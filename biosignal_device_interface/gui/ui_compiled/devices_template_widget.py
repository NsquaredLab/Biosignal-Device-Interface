# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'devices_template_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QScrollArea, QScrollBar,
    QSizePolicy, QSpacerItem, QStackedWidget, QWidget)

class Ui_DeviceWidgetForm(object):
    def setupUi(self, DeviceWidgetForm):
        if not DeviceWidgetForm.objectName():
            DeviceWidgetForm.setObjectName(u"DeviceWidgetForm")
        DeviceWidgetForm.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(DeviceWidgetForm.sizePolicy().hasHeightForWidth())
        DeviceWidgetForm.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(DeviceWidgetForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(DeviceWidgetForm)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.deviceSelectionComboBox = QComboBox(DeviceWidgetForm)
        self.deviceSelectionComboBox.setObjectName(u"deviceSelectionComboBox")

        self.gridLayout.addWidget(self.deviceSelectionComboBox, 0, 1, 1, 1)

        self.scrollAreaLayout = QHBoxLayout()
        self.scrollAreaLayout.setSpacing(6)
        self.scrollAreaLayout.setObjectName(u"scrollAreaLayout")
        self.scrollAreaLayout.setContentsMargins(20, -1, -1, -1)
        self.deviceScrollArea = QScrollArea(DeviceWidgetForm)
        self.deviceScrollArea.setObjectName(u"deviceScrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.deviceScrollArea.sizePolicy().hasHeightForWidth())
        self.deviceScrollArea.setSizePolicy(sizePolicy1)
        self.deviceScrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.deviceScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.deviceScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.deviceScrollArea.setWidgetResizable(True)
        self.deviceScrollAreaContents = QWidget()
        self.deviceScrollAreaContents.setObjectName(u"deviceScrollAreaContents")
        self.deviceScrollAreaContents.setGeometry(QRect(0, 0, 100, 30))
        self.deviceScrollAreaLayout = QHBoxLayout(self.deviceScrollAreaContents)
        self.deviceScrollAreaLayout.setObjectName(u"deviceScrollAreaLayout")
        self.deviceScrollAreaLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacerLeft = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.deviceScrollAreaLayout.addItem(self.horizontalSpacerLeft)

        self.deviceStackedWidget = QStackedWidget(self.deviceScrollAreaContents)
        self.deviceStackedWidget.setObjectName(u"deviceStackedWidget")

        self.deviceScrollAreaLayout.addWidget(self.deviceStackedWidget)

        self.horizontalSpacerRight = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.deviceScrollAreaLayout.addItem(self.horizontalSpacerRight)

        self.deviceScrollArea.setWidget(self.deviceScrollAreaContents)

        self.scrollAreaLayout.addWidget(self.deviceScrollArea)

        self.deviceScrollBar = QScrollBar(DeviceWidgetForm)
        self.deviceScrollBar.setObjectName(u"deviceScrollBar")
        self.deviceScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.scrollAreaLayout.addWidget(self.deviceScrollBar)


        self.gridLayout.addLayout(self.scrollAreaLayout, 1, 0, 1, 2)


        self.retranslateUi(DeviceWidgetForm)

        self.deviceStackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(DeviceWidgetForm)
    # setupUi

    def retranslateUi(self, DeviceWidgetForm):
        DeviceWidgetForm.setWindowTitle(QCoreApplication.translate("DeviceWidgetForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("DeviceWidgetForm", u"Device", None))
    # retranslateUi

