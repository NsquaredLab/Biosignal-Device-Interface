# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'otb_sessantaquattro_template_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_SessantaquattroForm(object):
    def setupUi(self, SessantaquattroForm):
        if not SessantaquattroForm.objectName():
            SessantaquattroForm.setObjectName(u"SessantaquattroForm")
        SessantaquattroForm.resize(400, 486)
        self.gridLayout_2 = QGridLayout(SessantaquattroForm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(SessantaquattroForm)
        self.widget.setObjectName(u"widget")
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.inputGroupBox = QGroupBox(self.widget)
        self.inputGroupBox.setObjectName(u"inputGroupBox")
        self.gridLayout_4 = QGridLayout(self.inputGroupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_10 = QLabel(self.inputGroupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)

        self.inputDetectionModeComboBox = QComboBox(self.inputGroupBox)
        self.inputDetectionModeComboBox.addItem("")
        self.inputDetectionModeComboBox.addItem("")
        self.inputDetectionModeComboBox.addItem("")
        self.inputDetectionModeComboBox.setObjectName(u"inputDetectionModeComboBox")

        self.gridLayout_4.addWidget(self.inputDetectionModeComboBox, 2, 1, 1, 1)

        self.inputLowResolutionRadioButton = QRadioButton(self.inputGroupBox)
        self.inputLowResolutionRadioButton.setObjectName(u"inputLowResolutionRadioButton")
        self.inputLowResolutionRadioButton.setChecked(True)

        self.gridLayout_4.addWidget(self.inputLowResolutionRadioButton, 1, 0, 1, 1)

        self.label_4 = QLabel(self.inputGroupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 2)

        self.inputHighResolutionRadioButton = QRadioButton(self.inputGroupBox)
        self.inputHighResolutionRadioButton.setObjectName(u"inputHighResolutionRadioButton")

        self.gridLayout_4.addWidget(self.inputHighResolutionRadioButton, 1, 1, 1, 1)

        self.label_5 = QLabel(self.inputGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)

        self.inputGainComboBox = QComboBox(self.inputGroupBox)
        self.inputGainComboBox.addItem("")
        self.inputGainComboBox.addItem("")
        self.inputGainComboBox.addItem("")
        self.inputGainComboBox.addItem("")
        self.inputGainComboBox.setObjectName(u"inputGainComboBox")

        self.gridLayout_4.addWidget(self.inputGainComboBox, 3, 1, 1, 1)


        self.gridLayout_5.addWidget(self.inputGroupBox, 2, 0, 1, 1)

        self.commandsGroupBox = QGroupBox(self.widget)
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


        self.gridLayout_5.addWidget(self.commandsGroupBox, 3, 0, 1, 1)

        self.acquisitionGroupBox = QGroupBox(self.widget)
        self.acquisitionGroupBox.setObjectName(u"acquisitionGroupBox")
        self.gridLayout = QGridLayout(self.acquisitionGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.acquisitionGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.acquisitionSamplingFrequencyComboBox = QComboBox(self.acquisitionGroupBox)
        self.acquisitionSamplingFrequencyComboBox.addItem("")
        self.acquisitionSamplingFrequencyComboBox.addItem("")
        self.acquisitionSamplingFrequencyComboBox.addItem("")
        self.acquisitionSamplingFrequencyComboBox.addItem("")
        self.acquisitionSamplingFrequencyComboBox.setObjectName(u"acquisitionSamplingFrequencyComboBox")

        self.gridLayout.addWidget(self.acquisitionSamplingFrequencyComboBox, 0, 1, 1, 1)

        self.acquisitionNumberOfChannelsComboBox = QComboBox(self.acquisitionGroupBox)
        self.acquisitionNumberOfChannelsComboBox.addItem("")
        self.acquisitionNumberOfChannelsComboBox.addItem("")
        self.acquisitionNumberOfChannelsComboBox.addItem("")
        self.acquisitionNumberOfChannelsComboBox.addItem("")
        self.acquisitionNumberOfChannelsComboBox.setObjectName(u"acquisitionNumberOfChannelsComboBox")

        self.gridLayout.addWidget(self.acquisitionNumberOfChannelsComboBox, 1, 1, 1, 1)

        self.label = QLabel(self.acquisitionGroupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.acquisitionGroupBox, 1, 0, 1, 1)

        self.connectionGroupBox = QGroupBox(self.widget)
        self.connectionGroupBox.setObjectName(u"connectionGroupBox")
        self.gridLayout_7 = QGridLayout(self.connectionGroupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_6 = QLabel(self.connectionGroupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)

        self.connectionIPLineEdit = QLineEdit(self.connectionGroupBox)
        self.connectionIPLineEdit.setObjectName(u"connectionIPLineEdit")

        self.gridLayout_7.addWidget(self.connectionIPLineEdit, 0, 1, 1, 1)

        self.label_7 = QLabel(self.connectionGroupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_7.addWidget(self.label_7, 1, 0, 1, 1)

        self.connectionPortLineEdit = QLineEdit(self.connectionGroupBox)
        self.connectionPortLineEdit.setObjectName(u"connectionPortLineEdit")

        self.gridLayout_7.addWidget(self.connectionPortLineEdit, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.connectionGroupBox, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.retranslateUi(SessantaquattroForm)

        self.acquisitionSamplingFrequencyComboBox.setCurrentIndex(0)
        self.acquisitionNumberOfChannelsComboBox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(SessantaquattroForm)
    # setupUi

    def retranslateUi(self, SessantaquattroForm):
        SessantaquattroForm.setWindowTitle(QCoreApplication.translate("SessantaquattroForm", u"Form", None))
        self.inputGroupBox.setTitle(QCoreApplication.translate("SessantaquattroForm", u"Input Parameters", None))
        self.label_10.setText(QCoreApplication.translate("SessantaquattroForm", u"Mode", None))
        self.inputDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SessantaquattroForm", u"MONOPOLAR", None))
        self.inputDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SessantaquattroForm", u"BIPOLAR", None))
        self.inputDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SessantaquattroForm", u"DIFFERENTIAL", None))

        self.inputLowResolutionRadioButton.setText(QCoreApplication.translate("SessantaquattroForm", u"16 Bit", None))
        self.label_4.setText(QCoreApplication.translate("SessantaquattroForm", u"Resolution", None))
        self.inputHighResolutionRadioButton.setText(QCoreApplication.translate("SessantaquattroForm", u"24 Bit", None))
        self.label_5.setText(QCoreApplication.translate("SessantaquattroForm", u"Gain", None))
        self.inputGainComboBox.setItemText(0, QCoreApplication.translate("SessantaquattroForm", u"Default", None))
        self.inputGainComboBox.setItemText(1, QCoreApplication.translate("SessantaquattroForm", u"Low", None))
        self.inputGainComboBox.setItemText(2, QCoreApplication.translate("SessantaquattroForm", u"Medium", None))
        self.inputGainComboBox.setItemText(3, QCoreApplication.translate("SessantaquattroForm", u"High", None))

        self.commandsGroupBox.setTitle(QCoreApplication.translate("SessantaquattroForm", u"Commands", None))
        self.commandConnectionPushButton.setText(QCoreApplication.translate("SessantaquattroForm", u"Connect", None))
        self.commandConfigurationPushButton.setText(QCoreApplication.translate("SessantaquattroForm", u"Configure", None))
        self.commandStreamPushButton.setText(QCoreApplication.translate("SessantaquattroForm", u"Stream", None))
        self.acquisitionGroupBox.setTitle(QCoreApplication.translate("SessantaquattroForm", u"Acquisiton Parameters", None))
        self.label_2.setText(QCoreApplication.translate("SessantaquattroForm", u"Number of Channels", None))
        self.acquisitionSamplingFrequencyComboBox.setItemText(0, QCoreApplication.translate("SessantaquattroForm", u"500", None))
        self.acquisitionSamplingFrequencyComboBox.setItemText(1, QCoreApplication.translate("SessantaquattroForm", u"1000", None))
        self.acquisitionSamplingFrequencyComboBox.setItemText(2, QCoreApplication.translate("SessantaquattroForm", u"2000", None))
        self.acquisitionSamplingFrequencyComboBox.setItemText(3, QCoreApplication.translate("SessantaquattroForm", u"4000", None))

        self.acquisitionNumberOfChannelsComboBox.setItemText(0, QCoreApplication.translate("SessantaquattroForm", u"8 Bio + 2 AUX + 2 ACC", None))
        self.acquisitionNumberOfChannelsComboBox.setItemText(1, QCoreApplication.translate("SessantaquattroForm", u"16 Bio + 2 AUX + 2 ACC", None))
        self.acquisitionNumberOfChannelsComboBox.setItemText(2, QCoreApplication.translate("SessantaquattroForm", u"32 Bio + 2 AUX + 2 ACC", None))
        self.acquisitionNumberOfChannelsComboBox.setItemText(3, QCoreApplication.translate("SessantaquattroForm", u"64 Bio + 2 AUX + 2 ACC", None))

        self.label.setText(QCoreApplication.translate("SessantaquattroForm", u"Sampling Frequency", None))
        self.connectionGroupBox.setTitle(QCoreApplication.translate("SessantaquattroForm", u"Connection parameters", None))
        self.label_6.setText(QCoreApplication.translate("SessantaquattroForm", u"IP", None))
        self.connectionIPLineEdit.setText(QCoreApplication.translate("SessantaquattroForm", u"127.0.0.1", None))
        self.label_7.setText(QCoreApplication.translate("SessantaquattroForm", u"Port", None))
        self.connectionPortLineEdit.setText(QCoreApplication.translate("SessantaquattroForm", u"31000", None))
    # retranslateUi

