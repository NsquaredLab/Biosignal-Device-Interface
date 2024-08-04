# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'muovi_template_widget.ui'
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

class Ui_MuoviForm(object):
    def setupUi(self, MuoviForm):
        if not MuoviForm.objectName():
            MuoviForm.setObjectName(u"MuoviForm")
        MuoviForm.resize(400, 324)
        self.gridLayout = QGridLayout(MuoviForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 86, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.connectionGroupBox = QGroupBox(MuoviForm)
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

        self.commandsGroupBox = QGroupBox(MuoviForm)
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

        self.inputGroupBox = QGroupBox(MuoviForm)
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


        self.retranslateUi(MuoviForm)

        self.inputDetectionModeComboBox.setCurrentIndex(1)
        self.inputWorkingModeComboBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MuoviForm)
    # setupUi

    def retranslateUi(self, MuoviForm):
        MuoviForm.setWindowTitle(QCoreApplication.translate("MuoviForm", u"MuoviForm", None))
        self.connectionGroupBox.setTitle(QCoreApplication.translate("MuoviForm", u"Connection parameters", None))
        self.connectionPortLabel.setText(QCoreApplication.translate("MuoviForm", u"54321", None))
        self.label_7.setText(QCoreApplication.translate("MuoviForm", u"Port", None))
        self.label_6.setText(QCoreApplication.translate("MuoviForm", u"IP", None))
        self.connectionUpdatePushButton.setText(QCoreApplication.translate("MuoviForm", u"Update", None))
        self.commandsGroupBox.setTitle(QCoreApplication.translate("MuoviForm", u"Commands", None))
        self.commandConnectionPushButton.setText(QCoreApplication.translate("MuoviForm", u"Connect", None))
        self.commandConfigurationPushButton.setText(QCoreApplication.translate("MuoviForm", u"Configure", None))
        self.commandStreamPushButton.setText(QCoreApplication.translate("MuoviForm", u"Stream", None))
        self.inputGroupBox.setTitle(QCoreApplication.translate("MuoviForm", u"Input Parameters", None))
        self.inputDetectionModeComboBox.setItemText(0, QCoreApplication.translate("MuoviForm", u"Monopolar - High Gain", None))
        self.inputDetectionModeComboBox.setItemText(1, QCoreApplication.translate("MuoviForm", u"Monopolar - Low Gain", None))
        self.inputDetectionModeComboBox.setItemText(2, QCoreApplication.translate("MuoviForm", u"Impedance Check", None))
        self.inputDetectionModeComboBox.setItemText(3, QCoreApplication.translate("MuoviForm", u"Test", None))

        self.label_10.setText(QCoreApplication.translate("MuoviForm", u"Detection Mode", None))
        self.label.setText(QCoreApplication.translate("MuoviForm", u"Working Mode", None))
        self.inputWorkingModeComboBox.setItemText(0, QCoreApplication.translate("MuoviForm", u"EEG", None))
        self.inputWorkingModeComboBox.setItemText(1, QCoreApplication.translate("MuoviForm", u"EMG", None))

    # retranslateUi

