# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'muovi_plus_template_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_MuoviPlusForm(object):
    def setupUi(self, MuoviPlusForm):
        if not MuoviPlusForm.objectName():
            MuoviPlusForm.setObjectName(u"MuoviPlusForm")
        MuoviPlusForm.resize(400, 324)
        self.gridLayout = QGridLayout(MuoviPlusForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 86, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.connectionGroupBox = QGroupBox(MuoviPlusForm)
        self.connectionGroupBox.setObjectName(u"connectionGroupBox")
        self.gridLayout_7 = QGridLayout(self.connectionGroupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.connectionPortLabel = QLabel(self.connectionGroupBox)
        self.connectionPortLabel.setObjectName(u"connectionPortLabel")

        self.gridLayout_7.addWidget(self.connectionPortLabel, 1, 1, 1, 1)

        self.label_7 = QLabel(self.connectionGroupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_7.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_6 = QLabel(self.connectionGroupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)

        self.connectionUpdatePushButton = QPushButton(self.connectionGroupBox)
        self.connectionUpdatePushButton.setObjectName(u"connectionUpdatePushButton")

        self.gridLayout_7.addWidget(self.connectionUpdatePushButton, 0, 2, 1, 1)

        self.connectionIPComboBox = QComboBox(self.connectionGroupBox)
        self.connectionIPComboBox.setObjectName(u"connectionIPComboBox")

        self.gridLayout_7.addWidget(self.connectionIPComboBox, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.connectionGroupBox, 0, 0, 1, 2)

        self.commandsGroupBox = QGroupBox(MuoviPlusForm)
        self.commandsGroupBox.setObjectName(u"commandsGroupBox")
        self.gridLayout_3 = QGridLayout(self.commandsGroupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.commandConnectionPushButton = QPushButton(self.commandsGroupBox)
        self.commandConnectionPushButton.setObjectName(u"commandConnectionPushButton")

        self.gridLayout_3.addWidget(self.commandConnectionPushButton, 0, 0, 1, 1)

        self.commandConfigurationPushButton = QPushButton(self.commandsGroupBox)
        self.commandConfigurationPushButton.setObjectName(u"commandConfigurationPushButton")

        self.gridLayout_3.addWidget(self.commandConfigurationPushButton, 1, 0, 1, 1)

        self.commandStreamPushButton = QPushButton(self.commandsGroupBox)
        self.commandStreamPushButton.setObjectName(u"commandStreamPushButton")

        self.gridLayout_3.addWidget(self.commandStreamPushButton, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.commandsGroupBox, 2, 0, 2, 2)

        self.inputGroupBox = QGroupBox(MuoviPlusForm)
        self.inputGroupBox.setObjectName(u"inputGroupBox")
        self.gridLayout_4 = QGridLayout(self.inputGroupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.inputDetectionModeComboBox = QComboBox(self.inputGroupBox)
        self.inputDetectionModeComboBox.addItem("")
        self.inputDetectionModeComboBox.addItem("")
        self.inputDetectionModeComboBox.addItem("")
        self.inputDetectionModeComboBox.addItem("")
        self.inputDetectionModeComboBox.setObjectName(u"inputDetectionModeComboBox")

        self.gridLayout_4.addWidget(self.inputDetectionModeComboBox, 1, 1, 1, 1)

        self.label_10 = QLabel(self.inputGroupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 1)

        self.label = QLabel(self.inputGroupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.inputWorkingModeComboBox = QComboBox(self.inputGroupBox)
        self.inputWorkingModeComboBox.addItem("")
        self.inputWorkingModeComboBox.addItem("")
        self.inputWorkingModeComboBox.setObjectName(u"inputWorkingModeComboBox")

        self.gridLayout_4.addWidget(self.inputWorkingModeComboBox, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.inputGroupBox, 1, 0, 1, 2)


        self.retranslateUi(MuoviPlusForm)

        self.inputDetectionModeComboBox.setCurrentIndex(1)
        self.inputWorkingModeComboBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MuoviPlusForm)
    # setupUi

    def retranslateUi(self, MuoviPlusForm):
        MuoviPlusForm.setWindowTitle(QCoreApplication.translate("MuoviPlusForm", u"MuoviPlusForm", None))
        self.connectionGroupBox.setTitle(QCoreApplication.translate("MuoviPlusForm", u"Connection parameters", None))
        self.connectionPortLabel.setText(QCoreApplication.translate("MuoviPlusForm", u"54321", None))
        self.label_7.setText(QCoreApplication.translate("MuoviPlusForm", u"Port", None))
        self.label_6.setText(QCoreApplication.translate("MuoviPlusForm", u"IP", None))
        self.connectionUpdatePushButton.setText(QCoreApplication.translate("MuoviPlusForm", u"Update", None))
        self.commandsGroupBox.setTitle(QCoreApplication.translate("MuoviPlusForm", u"Commands", None))
        self.commandConnectionPushButton.setText(QCoreApplication.translate("MuoviPlusForm", u"Connect", None))
        self.commandConfigurationPushButton.setText(QCoreApplication.translate("MuoviPlusForm", u"Configure", None))
        self.commandStreamPushButton.setText(QCoreApplication.translate("MuoviPlusForm", u"Stream", None))
        self.inputGroupBox.setTitle(QCoreApplication.translate("MuoviPlusForm", u"Input Parameters", None))
        self.inputDetectionModeComboBox.setItemText(0, QCoreApplication.translate("MuoviPlusForm", u"Monopolar - High Gain", None))
        self.inputDetectionModeComboBox.setItemText(1, QCoreApplication.translate("MuoviPlusForm", u"Monopolar - Low Gain", None))
        self.inputDetectionModeComboBox.setItemText(2, QCoreApplication.translate("MuoviPlusForm", u"Impedance Check", None))
        self.inputDetectionModeComboBox.setItemText(3, QCoreApplication.translate("MuoviPlusForm", u"Test", None))

        self.label_10.setText(QCoreApplication.translate("MuoviPlusForm", u"Detection Mode", None))
        self.label.setText(QCoreApplication.translate("MuoviPlusForm", u"Working Mode", None))
        self.inputWorkingModeComboBox.setItemText(0, QCoreApplication.translate("MuoviPlusForm", u"EEG", None))
        self.inputWorkingModeComboBox.setItemText(1, QCoreApplication.translate("MuoviPlusForm", u"EMG", None))

    # retranslateUi

