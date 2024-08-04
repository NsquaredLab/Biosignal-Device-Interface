# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'devices_template_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QSizePolicy, QStackedWidget, QWidget)

class Ui_DeviceWidgetForm(object):
    def setupUi(self, DeviceWidgetForm):
        if not DeviceWidgetForm.objectName():
            DeviceWidgetForm.setObjectName(u"DeviceWidgetForm")
        DeviceWidgetForm.resize(400, 300)
        self.gridLayout = QGridLayout(DeviceWidgetForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(DeviceWidgetForm)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.deviceSelectionComboBox = QComboBox(DeviceWidgetForm)
        self.deviceSelectionComboBox.setObjectName(u"deviceSelectionComboBox")

        self.gridLayout.addWidget(self.deviceSelectionComboBox, 0, 1, 1, 1)

        self.deviceStackedWidget = QStackedWidget(DeviceWidgetForm)
        self.deviceStackedWidget.setObjectName(u"deviceStackedWidget")

        self.gridLayout.addWidget(self.deviceStackedWidget, 1, 0, 1, 2)


        self.retranslateUi(DeviceWidgetForm)

        self.deviceStackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(DeviceWidgetForm)
    # setupUi

    def retranslateUi(self, DeviceWidgetForm):
        DeviceWidgetForm.setWindowTitle(QCoreApplication.translate("DeviceWidgetForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("DeviceWidgetForm", u"Device", None))
    # retranslateUi

