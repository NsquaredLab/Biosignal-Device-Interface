import numpy as np

COLOR_PALETTE_DARK = [
    "#EF9A9A",
    "#F48FB1",
    "#CE93D8",
    "#B39DDB",
    "#9FA8DA",
    "#90CAF9",
    "#81D4FA",
    "#80DEEA",
    "#80CBC4",
    "#A5D6A7",
    "#C5E1A5",
    "#E6EE9C",
    "#FFF59D",
    "#FFE082",
    "#FFCC80",
    "#FFAB91",
    "#BCAAA4",
    "#EEEEEE",
    "#B0BEC5",
]

COLOR_PALETTE_LIGHT = [
    "#F44336",
    "#E91E63",
    "#9C27B0",
    "#673AB7",
    "#3F51B5",
    "#2196F3",
    "#03A9F4",
    "#00BCD4",
    "#009688",
    "#4CAF50",
    "#8BC34A",
    "#CDDC39",
    "#FFEB3B",
    "#FFC107",
    "#FF9800",
    "#FF5722",
    "#795548",
    "#9E9E9E",
    "#607D8B",
]

COLOR_PALETTE_RGB_DARK = np.array(
    [
        tuple(int(hex_color[i : i + 2], 16) for i in (1, 3, 5))
        for hex_color in COLOR_PALETTE_DARK
    ]
).astype(np.float32)

COLOR_PALETTE_RGB_LIGHT = np.array(
    [
        tuple(int(hex_color[i : i + 2], 16) for i in (1, 3, 5))
        for hex_color in COLOR_PALETTE_LIGHT
    ]
).astype(np.float32)
