from __future__ import annotations
from functools import partial
from typing import TYPE_CHECKING

from PySide6.QtGui import QResizeEvent, QWheelEvent
from vispy import app, gloo
from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QScrollArea,
    QCheckBox,
    QGridLayout,
    QSizePolicy,
)
from PySide6.QtCore import Qt, Signal, QPoint
import matplotlib.colors as mcolors
import numpy as np
from scipy.signal import resample

from biosignal_device_interface.constants.plots.color_palette import (
    COLOR_PALETTE_RGB_DARK,
    COLOR_PALETTE_RGB_LIGHT,
)


class BiosignalPlotWidget(QWidget):
    bad_channels_updated: Signal = Signal(np.ndarray)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_window = parent
        self.number_of_lines: int | None = None
        self.number_of_vertices: int | None = None
        self.internal_sampling_frequency_threshold = 256
        self.external_sampling_frequency: int | None = None
        self.internal_sampling_frequency: int | None = None
        self.sampling_factor: int | None = None
        self.downsample_buffer: np.ndarray | None = None

        self.line_checkboxes: list[QCheckBox] = []
        self.lines_enabled: np.ndarray | None = None

        self.canvas_layout: QVBoxLayout | None = None

        self.color_dict = mcolors.CSS4_COLORS

        self._configure_widget()

        self.is_configured: bool = False

    def _configure_widget(self):
        # Create scroll_area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )  # Disable horizontal scrollbar
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.scroll_area.setLayoutDirection(Qt.RightToLeft)

        # Create a layout for the VispyFastPlotWidget
        self.setLayout(QVBoxLayout())
        # Add the scroll_area to the layout
        self.layout().addWidget(self.scroll_area)

        # Create a layout for the Scroll Area
        self.scroll_area_layout = QVBoxLayout()
        # Add the layout to the scroll_area
        self.scroll_area.setLayout(self.scroll_area_layout)

        # Make the plot_widget a child of the scroll_area
        self.container_widget = QWidget()
        self.container_widget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

        self.scroll_area.setWidget(self.container_widget)

        self.container_widget_layout = QGridLayout()
        self.container_widget.setLayout(self.container_widget_layout)
        self.container_widget.setLayoutDirection(Qt.LeftToRight)

        self.container_widget_layout.setColumnStretch(0, 0)
        self.container_widget_layout.setColumnStretch(1, 1)

        self.canvas = VispyFastPlotCanvas(
            parent=self.main_window, scroll_area=self.scroll_area
        )

        self.max_texture_size = gloo.gl.glGetParameter(gloo.gl.GL_MAX_TEXTURE_SIZE)
        self.plot_widget = self.canvas.native
        self.container_widget_layout.addWidget(self.plot_widget, 0, 1, 0, 1)

    def configure(
        self,
        lines: int,
        sampling_frequency: int = 2000,
        plot_sampling_frequency: int | None = None,
        display_time: int = 10,
        line_height: int = 50,
        background_color: np.ndarray = np.array([18.0, 18.0, 18.0, 1]),
    ):
        self.number_of_lines = lines
        self.external_sampling_frequency = sampling_frequency
        if plot_sampling_frequency is not None:
            self.internal_sampling_frequency_threshold = plot_sampling_frequency

        if (
            self.external_sampling_frequency
            > self.internal_sampling_frequency_threshold
        ):
            self.sampling_factor = int(
                self.external_sampling_frequency
                / self.internal_sampling_frequency_threshold
            )

            self.internal_sampling_frequency = (
                self.external_sampling_frequency // self.sampling_factor
            )

        else:
            self.internal_sampling_frequency = self.external_sampling_frequency

        self.number_of_vertices = int(display_time * self.internal_sampling_frequency)

        background_color = self._check_background_color_for_format(background_color)
        self.setStyleSheet(
            f"background-color: rgba({background_color[0]}, {background_color[1]}, {background_color[2]}, {background_color[3]});"
        )
        self.container_widget.setStyleSheet(
            f"background-color: rgba({background_color[0]}, {background_color[1]}, {background_color[2]}, {background_color[3]});"
        )

        self.space_for_each_line = min(
            int(self.max_texture_size // self.number_of_lines // 1.5), line_height
        )

        self.canvas.configure(
            self.number_of_lines, self.number_of_vertices, background_color
        )

        # Clear the layout
        for i in reversed(range(self.container_widget_layout.rowCount())):
            # Remove the widget from the layout
            if self.container_widget_layout.itemAt(i) is not None:
                self.container_widget_layout.itemAt(i).widget().setParent(None)

        lines_space = self.space_for_each_line * self.number_of_lines
        self.container_widget.setFixedHeight((lines_space))

        self.line_checkboxes = []
        self.number_of_lines_enabled = []
        self.lines_enabled = np.ones((self.number_of_lines,)).astype(bool)

        for i in range(self.number_of_lines):
            checkbox = QCheckBox(f"Line {i + 1}")
            checkbox.setChecked(True)
            checkbox.stateChanged.connect(partial(self._toggle_line, i))
            checkbox.setStyleSheet("padding-left: 10px;")
            checkbox.setFixedHeight(self.space_for_each_line)
            self.line_checkboxes.append(checkbox)
            self.container_widget_layout.addWidget(checkbox, i, 0)

        self.container_widget_layout.removeWidget(self.plot_widget)
        self.container_widget_layout.addWidget(
            self.plot_widget, 0, 1, self.number_of_lines, 1
        )

        # Set the standardized height for each row
        for i in range(self.container_widget_layout.rowCount()):
            if i < self.number_of_lines:
                self.container_widget_layout.setRowMinimumHeight(
                    i, self.space_for_each_line
                )  # Set the minimum height of each row to 100 pixels
            else:
                self.container_widget_layout.setRowMinimumHeight(i, 0)

        self.is_configured = True

    def update_plot(self, input_data: np.ndarray) -> None:
        # Downsample input_data with external sampling frequency to match internal sampling frequency
        if self.external_sampling_frequency != self.internal_sampling_frequency:
            if self.downsample_buffer is not None:
                input_data = np.hstack((self.downsample_buffer, input_data))
                self.downsample_buffer = None

            input_samples = input_data.shape[1]
            left_over_samples = input_samples % self.sampling_factor
            if left_over_samples > 0:
                self.downsample_buffer = input_data[:, -left_over_samples:]
                input_data = input_data[:, :-left_over_samples]
            output_samples = input_samples // self.sampling_factor
            input_data = resample(
                input_data,
                output_samples,
                axis=1,
            )

        self.canvas.on_update(input_data)

    def reset_data(self) -> None:
        self.canvas.on_reset()

    def _toggle_line(self, line_number: int, state: int) -> None:
        is_checked = state == 2
        self.lines_enabled[line_number] = is_checked
        self.canvas.on_update_color(line_number, not is_checked)
        self.bad_channels_updated.emit(self.lines_enabled)

    def set_lines_enabled(self, indices: list) -> None:
        self.lines_enabled = np.ones((self.number_of_lines,)).astype(bool)
        self.lines_enabled[indices] = False

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.container_widget.setFixedWidth(self.scroll_area.width())

        return super().resizeEvent(event)

    def _check_background_color_for_format(
        self, input_color: str | list | np.ndarray
    ) -> np.ndarray:
        if isinstance(input_color, str):
            if input_color.startswith("#"):
                input_color = np.array(
                    [int(input_color[i : i + 2], 16) / 255 for i in (1, 3, 5)] + [1]
                )
            elif input_color.startswith("rgb"):
                input_color = np.array(
                    [int(i) for i in input_color[4:-1].split(",")] + [1]
                )
            elif input_color.startswith("rgba"):
                input_color = np.array([int(i) for i in input_color[5:-1].split(",")])
            # Check if color is given as "red" or "blue" etc.
            elif input_color in self.color_dict:
                input_color = np.array(
                    [
                        int(self.color_dict[input_color][i : i + 2], 16) / 255
                        for i in (1, 3, 5)
                    ]
                    + [1]
                )

        elif isinstance(input_color, list):
            input_color = np.array(input_color)

        if np.max(input_color) > 1:
            input_color = input_color / 255

        if input_color.shape[0] == 3:
            input_color = np.append(input_color, 1)

        return input_color


class VispyFastPlotCanvas(app.Canvas):
    def __init__(self, scroll_area: QScrollArea, parent=None):
        super().__init__(keys=None, parent=parent)

        self.main_widget = parent
        self.plot_scroll_area = scroll_area
        self.line_data = None
        self.line_colors = None
        self._init_shaders()
        self.program = gloo.Program(self.vert_shader, self.frag_shader)

        self.background_color: np.ndarray = None

    def configure(
        self,
        lines: int,
        vertices: int,
        background_color: np.ndarray = np.array([18.0, 18.0, 18.0]),
        line_color: np.ndarray | None = None,
    ):
        """_summary_

        Args:
            lines (int): _description_
            vertices (int): _description_
            background_color (str | np.ndarray, optional): _description_. Defaults to "black".
            line_color (np.ndarray | None, optional): Numpy array of rgb value(s). RGB values range between 0 and 255. Defaults to None.
        """

        self.lines = lines
        self.vertices = vertices
        self.background_color = background_color

        # Generate template signal
        self.line_data = np.zeros((self.lines, self.vertices)).astype(np.float32)

        colors = []
        if line_color is None:
            for line in range(self.lines):
                if self.is_light_color(self.background_color):
                    colors.append(
                        COLOR_PALETTE_RGB_LIGHT[line % len(COLOR_PALETTE_RGB_LIGHT)]
                        / 255.0
                    )
                else:
                    colors.append(
                        COLOR_PALETTE_RGB_DARK[line % len(COLOR_PALETTE_RGB_DARK)]
                        / 255.0
                    )
        else:
            for line in range(self.lines):
                colors.append(line_color[line % len(line_color)] / 255.0)

        self.line_colors = np.repeat(colors, self.vertices, axis=0)

        self.index = np.c_[
            np.repeat(np.repeat(np.arange(1), self.lines), self.vertices),
            np.repeat(np.tile(np.arange(self.lines), 1), self.vertices),
            np.tile(np.arange(self.vertices), self.lines),
        ].astype(np.float32)

        # Setup Program
        self.program["a_position"] = self.line_data.reshape(-1, 1)
        self.program["a_color"] = self.line_colors
        self.program["a_index"] = self.index
        self.program["u_scale"] = (1.0, 1.0)
        self.program["u_size"] = (self.lines, 1)
        self.program["u_n"] = self.vertices

        gloo.set_viewport(0, 0, *self.physical_size)
        gloo.set_state(
            clear_color=self.background_color,
            blend=True,
            blend_func=("src_alpha", "one_minus_src_alpha"),
        )

    def on_update(self, input_data: np.ndarray) -> None:
        input_lines = input_data.shape[0]
        input_vertices = input_data.shape[1]

        assert (
            input_lines == self.lines
        ), "Input data lines do not match the configured lines."

        # Flip the order of the input lines backwards
        input_data = np.flip(input_data, axis=0)

        # Check if the input data has more vertices than the configured vertices
        if input_vertices > self.vertices:
            self.line_data = input_data[:, -self.vertices :]
        else:
            self.line_data[:, :-input_vertices] = self.line_data[:, input_vertices:]
            self.line_data[:, -input_vertices:] = input_data

        plot_data = self.line_data.ravel().astype(np.float32)
        self.program["a_position"].set_data(plot_data)
        self.update()
        self.context.flush()

    def on_update_color(self, line_number: int, disable: bool = False) -> None:
        # Update alpha value of the line color
        disable_color = self.background_color
        fliped_line_number = self.lines - line_number - 1
        if disable:
            self.line_colors[
                fliped_line_number
                * self.vertices : (fliped_line_number + 1)
                * self.vertices
            ] = disable_color[:3]
        else:

            if self.is_light_color(self.background_color):
                self.line_colors[
                    fliped_line_number
                    * self.vertices : (fliped_line_number + 1)
                    * self.vertices
                ] = (
                    COLOR_PALETTE_RGB_LIGHT[
                        fliped_line_number % len(COLOR_PALETTE_RGB_LIGHT)
                    ]
                    / 255.0
                )
            else:
                self.line_colors[
                    fliped_line_number
                    * self.vertices : (fliped_line_number + 1)
                    * self.vertices
                ] = (
                    COLOR_PALETTE_RGB_DARK[
                        fliped_line_number % len(COLOR_PALETTE_RGB_DARK)
                    ]
                    / 255.0
                )

        self.program["a_color"].set_data(self.line_colors)
        self.update()
        self.context.flush()

    def on_reset(self):
        self.line_data = np.zeros((self.lines, self.vertices)).astype(np.float32)
        self.program["a_position"].set_data(self.line_data.ravel().astype(np.float32))
        self.update()
        self.context.flush()

    def on_resize(self, event):
        gloo.set_viewport(0, 0, *event.physical_size)

    def on_draw(self, event):
        if self.line_data is None:
            return

        gloo.clear()
        self.program.draw("line_strip")

    def on_mouse_wheel(self, event):
        # Get the delta from the mouse event
        dx, dy = event.delta

        scale_factor = 15
        dx *= scale_factor
        dy *= scale_factor
        # Create a QWheelEvent
        pos = QPoint(event.pos[0], event.pos[1])
        global_pos = QPoint(event.pos[0], event.pos[1])
        pixel_delta = QPoint(dx, dy)
        angle_delta = QPoint(dx * 8, dy * 8)  # Convert to eighths of a degree
        buttons = Qt.NoButton
        modifiers = Qt.NoModifier
        phase = Qt.ScrollUpdate
        inverted = False

        wheel_event = QWheelEvent(
            pos,
            global_pos,
            pixel_delta,
            angle_delta,
            buttons,
            modifiers,
            phase,
            inverted,
        )

        self.plot_scroll_area.wheelEvent(wheel_event)

    def is_light_color(self, rgb):
        # Normalize to 1
        luminance = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
        return luminance > 0.5

    def _init_shaders(self):
        self.vert_shader = """
        #version 120
        // y coordinate of the position.
        attribute float a_position;
        // row, col, and time index.
        attribute vec3 a_index;
        varying vec3 v_index;
        // 2D scaling factor (zooming).
        uniform vec2 u_scale;
        // Size of the table.
        uniform vec2 u_size;
        // Number of samples per signal.
        uniform float u_n;
        // Color.
        attribute vec3 a_color;
        varying vec4 v_color;
        // Varying variables used for clipping in the fragment shader.
        varying vec2 v_position;
        varying vec4 v_ab;
        void main() {
            float nrows = u_size.x;
            float ncols = u_size.y;
            // Compute the x coordinate from the time index.
            float x = -1 + 2*a_index.z / (u_n-1);
            vec2 position = vec2(x - (1 - 1 / u_scale.x), a_position);
            // Find the affine transformation for the subplots.
            vec2 a = vec2(1./ncols, 1./nrows)*.9;
            vec2 b = vec2(-1 + 2*(a_index.x+.5) / ncols,
                          -1 + 2*(a_index.y+.5) / nrows);
            // Apply the static subplot transformation + scaling.
            gl_Position = vec4(a*u_scale*position+b, 0.0, 1.0);
            v_color = vec4(a_color, 1.);
            v_index = a_index;
            // For clipping test in the fragment shader.
            v_position = gl_Position.xy;
            v_ab = vec4(a, b);
        }
        """

        self.frag_shader = """
        #version 120
        varying vec4 v_color;
        varying vec3 v_index;
        varying vec2 v_position;
        varying vec4 v_ab;
        void main() {
            gl_FragColor = v_color;
            // Discard the fragments between the signals (emulate glMultiDrawArrays).
            if ((fract(v_index.x) > 0.) || (fract(v_index.y) > 0.))
                discard;
            // Clipping test.
            vec2 test = abs((v_position.xy-v_ab.zw)/v_ab.xy);
            if ((test.x > 1) || (test.y > 1))
                discard;
        }
        """
