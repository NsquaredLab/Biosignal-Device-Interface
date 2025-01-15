# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'otb_quattrocento_template_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_QuattrocentoForm(object):
    def setupUi(self, QuattrocentoForm):
        if not QuattrocentoForm.objectName():
            QuattrocentoForm.setObjectName(u"QuattrocentoForm")
        QuattrocentoForm.resize(400, 638)
        self.gridLayout_2 = QGridLayout(QuattrocentoForm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(QuattrocentoForm)
        self.widget.setObjectName(u"widget")
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.inputGroupBox = QGroupBox(self.widget)
        self.inputGroupBox.setObjectName(u"inputGroupBox")
        self.gridLayout_4 = QGridLayout(self.inputGroupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.inputGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.inputDetectionModeComboBox = QComboBox(self.inputGroupBox)
        self.inputDetectionModeComboBox.addItem("")
        self.inputDetectionModeComboBox.addItem("")
        self.inputDetectionModeComboBox.addItem("")
        self.inputDetectionModeComboBox.setObjectName(u"inputDetectionModeComboBox")

        self.gridLayout_4.addWidget(self.inputDetectionModeComboBox, 3, 1, 1, 1)

        self.label_10 = QLabel(self.inputGroupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_9 = QLabel(self.inputGroupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1)

        self.inputHighPassComboBox = QComboBox(self.inputGroupBox)
        self.inputHighPassComboBox.addItem("")
        self.inputHighPassComboBox.addItem("")
        self.inputHighPassComboBox.addItem("")
        self.inputHighPassComboBox.addItem("")
        self.inputHighPassComboBox.setObjectName(u"inputHighPassComboBox")

        self.gridLayout_4.addWidget(self.inputHighPassComboBox, 1, 1, 1, 1)

        self.label_8 = QLabel(self.inputGroupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)

        self.inputLowPassComboBox = QComboBox(self.inputGroupBox)
        self.inputLowPassComboBox.addItem("")
        self.inputLowPassComboBox.addItem("")
        self.inputLowPassComboBox.addItem("")
        self.inputLowPassComboBox.addItem("")
        self.inputLowPassComboBox.setObjectName(u"inputLowPassComboBox")

        self.gridLayout_4.addWidget(self.inputLowPassComboBox, 2, 1, 1, 1)

        self.inputChannelComboBox = QComboBox(self.inputGroupBox)
        self.inputChannelComboBox.addItem("")
        self.inputChannelComboBox.addItem("")
        self.inputChannelComboBox.addItem("")
        self.inputChannelComboBox.addItem("")
        self.inputChannelComboBox.addItem("")
        self.inputChannelComboBox.addItem("")
        self.inputChannelComboBox.setObjectName(u"inputChannelComboBox")
        self.inputChannelComboBox.setEnabled(False)

        self.gridLayout_4.addWidget(self.inputChannelComboBox, 0, 1, 1, 1)

        self.inputConfigurationPushButton = QPushButton(self.inputGroupBox)
        self.inputConfigurationPushButton.setObjectName(u"inputConfigurationPushButton")
        self.inputConfigurationPushButton.setEnabled(False)

        self.gridLayout_4.addWidget(self.inputConfigurationPushButton, 4, 1, 1, 1)


        self.gridLayout_6.addWidget(self.inputGroupBox, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 5, 0, 1, 1)

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


        self.gridLayout_6.addWidget(self.commandsGroupBox, 4, 0, 1, 1)

        self.acquisitionGroupBox = QGroupBox(self.widget)
        self.acquisitionGroupBox.setObjectName(u"acquisitionGroupBox")
        self.gridLayout = QGridLayout(self.acquisitionGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.acquisitionNumberOfChannelsComboBox = QComboBox(self.acquisitionGroupBox)
        self.acquisitionNumberOfChannelsComboBox.addItem("")
        self.acquisitionNumberOfChannelsComboBox.addItem("")
        self.acquisitionNumberOfChannelsComboBox.addItem("")
        self.acquisitionNumberOfChannelsComboBox.addItem("")
        self.acquisitionNumberOfChannelsComboBox.setObjectName(u"acquisitionNumberOfChannelsComboBox")

        self.gridLayout.addWidget(self.acquisitionNumberOfChannelsComboBox, 1, 1, 1, 1)

        self.acquisitionSamplingFrequencyComboBox = QComboBox(self.acquisitionGroupBox)
        self.acquisitionSamplingFrequencyComboBox.addItem("")
        self.acquisitionSamplingFrequencyComboBox.addItem("")
        self.acquisitionSamplingFrequencyComboBox.addItem("")
        self.acquisitionSamplingFrequencyComboBox.addItem("")
        self.acquisitionSamplingFrequencyComboBox.setObjectName(u"acquisitionSamplingFrequencyComboBox")

        self.gridLayout.addWidget(self.acquisitionSamplingFrequencyComboBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.acquisitionGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.acquisitionGroupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.acquisitionDecimatorCheckBox = QCheckBox(self.acquisitionGroupBox)
        self.acquisitionDecimatorCheckBox.setObjectName(u"acquisitionDecimatorCheckBox")
        self.acquisitionDecimatorCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.acquisitionDecimatorCheckBox, 2, 0, 1, 1)

        self.acquisitionRecordingCheckBox = QCheckBox(self.acquisitionGroupBox)
        self.acquisitionRecordingCheckBox.setObjectName(u"acquisitionRecordingCheckBox")
        self.acquisitionRecordingCheckBox.setEnabled(False)

        self.gridLayout.addWidget(self.acquisitionRecordingCheckBox, 2, 1, 1, 1)


        self.gridLayout_6.addWidget(self.acquisitionGroupBox, 1, 0, 1, 1)

        self.gridSelectionGroupBox = QGroupBox(self.widget)
        self.gridSelectionGroupBox.setObjectName(u"gridSelectionGroupBox")
        self.gridLayout_5 = QGridLayout(self.gridSelectionGroupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridFourCheckBox = QCheckBox(self.gridSelectionGroupBox)
        self.gridFourCheckBox.setObjectName(u"gridFourCheckBox")

        self.gridLayout_5.addWidget(self.gridFourCheckBox, 1, 1, 1, 1)

        self.gridThreeCheckBox = QCheckBox(self.gridSelectionGroupBox)
        self.gridThreeCheckBox.setObjectName(u"gridThreeCheckBox")

        self.gridLayout_5.addWidget(self.gridThreeCheckBox, 1, 0, 1, 1)

        self.gridFiveCheckBox = QCheckBox(self.gridSelectionGroupBox)
        self.gridFiveCheckBox.setObjectName(u"gridFiveCheckBox")

        self.gridLayout_5.addWidget(self.gridFiveCheckBox, 1, 2, 1, 1)

        self.gridSixCheckBox = QCheckBox(self.gridSelectionGroupBox)
        self.gridSixCheckBox.setObjectName(u"gridSixCheckBox")

        self.gridLayout_5.addWidget(self.gridSixCheckBox, 1, 3, 1, 1)

        self.gridTwoCheckBox = QCheckBox(self.gridSelectionGroupBox)
        self.gridTwoCheckBox.setObjectName(u"gridTwoCheckBox")
        self.gridTwoCheckBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_5.addWidget(self.gridTwoCheckBox, 0, 3, 1, 1)

        self.gridOneCheckBox = QCheckBox(self.gridSelectionGroupBox)
        self.gridOneCheckBox.setObjectName(u"gridOneCheckBox")

        self.gridLayout_5.addWidget(self.gridOneCheckBox, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.gridSelectionGroupBox, 3, 0, 1, 1)

        self.connectionGroupBox = QGroupBox(self.widget)
        self.connectionGroupBox.setObjectName(u"connectionGroupBox")
        self.gridLayout_7 = QGridLayout(self.connectionGroupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_4 = QLabel(self.connectionGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)

        self.connectionIPLineEdit = QLineEdit(self.connectionGroupBox)
        self.connectionIPLineEdit.setObjectName(u"connectionIPLineEdit")

        self.gridLayout_7.addWidget(self.connectionIPLineEdit, 0, 1, 1, 1)

        self.label_5 = QLabel(self.connectionGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 1, 0, 1, 1)

        self.connectionPortLineEdit = QLineEdit(self.connectionGroupBox)
        self.connectionPortLineEdit.setObjectName(u"connectionPortLineEdit")

        self.gridLayout_7.addWidget(self.connectionPortLineEdit, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.connectionGroupBox, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(QuattrocentoForm)

        self.inputHighPassComboBox.setCurrentIndex(1)
        self.inputLowPassComboBox.setCurrentIndex(1)
        self.acquisitionNumberOfChannelsComboBox.setCurrentIndex(3)
        self.acquisitionSamplingFrequencyComboBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(QuattrocentoForm)
    # setupUi

    def retranslateUi(self, QuattrocentoForm):
        QuattrocentoForm.setWindowTitle(QCoreApplication.translate("QuattrocentoForm", u"Form", None))
        self.inputGroupBox.setTitle(QCoreApplication.translate("QuattrocentoForm", u"Input Parameters", None))
        self.label_3.setText(QCoreApplication.translate("QuattrocentoForm", u"Select Channel", None))
        self.inputDetectionModeComboBox.setItemText(0, QCoreApplication.translate("QuattrocentoForm", u"MONOPOLAR", None))
        self.inputDetectionModeComboBox.setItemText(1, QCoreApplication.translate("QuattrocentoForm", u"DIFFERENTIAL", None))
        self.inputDetectionModeComboBox.setItemText(2, QCoreApplication.translate("QuattrocentoForm", u"BIPOLAR", None))

        self.label_10.setText(QCoreApplication.translate("QuattrocentoForm", u"Mode", None))
        self.label_9.setText(QCoreApplication.translate("QuattrocentoForm", u"Low Pass", None))
        self.inputHighPassComboBox.setItemText(0, QCoreApplication.translate("QuattrocentoForm", u"0.7 Hz", None))
        self.inputHighPassComboBox.setItemText(1, QCoreApplication.translate("QuattrocentoForm", u"10 Hz", None))
        self.inputHighPassComboBox.setItemText(2, QCoreApplication.translate("QuattrocentoForm", u"100 Hz", None))
        self.inputHighPassComboBox.setItemText(3, QCoreApplication.translate("QuattrocentoForm", u"200 Hz", None))

        self.label_8.setText(QCoreApplication.translate("QuattrocentoForm", u"High Pass", None))
        self.inputLowPassComboBox.setItemText(0, QCoreApplication.translate("QuattrocentoForm", u"130 Hz", None))
        self.inputLowPassComboBox.setItemText(1, QCoreApplication.translate("QuattrocentoForm", u"500 Hz", None))
        self.inputLowPassComboBox.setItemText(2, QCoreApplication.translate("QuattrocentoForm", u"900 Hz", None))
        self.inputLowPassComboBox.setItemText(3, QCoreApplication.translate("QuattrocentoForm", u"4400 Hz", None))

        self.inputChannelComboBox.setItemText(0, QCoreApplication.translate("QuattrocentoForm", u"IN1-4", None))
        self.inputChannelComboBox.setItemText(1, QCoreApplication.translate("QuattrocentoForm", u"IN5-8", None))
        self.inputChannelComboBox.setItemText(2, QCoreApplication.translate("QuattrocentoForm", u"MULTIPLE_IN_1", None))
        self.inputChannelComboBox.setItemText(3, QCoreApplication.translate("QuattrocentoForm", u"MULTIPLE_IN_2", None))
        self.inputChannelComboBox.setItemText(4, QCoreApplication.translate("QuattrocentoForm", u"MULTIPLE_IN_3", None))
        self.inputChannelComboBox.setItemText(5, QCoreApplication.translate("QuattrocentoForm", u"MULTIPLE_IN_4", None))

        self.inputConfigurationPushButton.setText(QCoreApplication.translate("QuattrocentoForm", u"Configure Input", None))
        self.commandsGroupBox.setTitle(QCoreApplication.translate("QuattrocentoForm", u"Commands", None))
        self.commandConnectionPushButton.setText(QCoreApplication.translate("QuattrocentoForm", u"Connect", None))
        self.commandConfigurationPushButton.setText(QCoreApplication.translate("QuattrocentoForm", u"Configure", None))
        self.commandStreamPushButton.setText(QCoreApplication.translate("QuattrocentoForm", u"Stream", None))
        self.acquisitionGroupBox.setTitle(QCoreApplication.translate("QuattrocentoForm", u"Acquisiton Parameters", None))
        self.acquisitionNumberOfChannelsComboBox.setItemText(0, QCoreApplication.translate("QuattrocentoForm", u"120", None))
        self.acquisitionNumberOfChannelsComboBox.setItemText(1, QCoreApplication.translate("QuattrocentoForm", u"216", None))
        self.acquisitionNumberOfChannelsComboBox.setItemText(2, QCoreApplication.translate("QuattrocentoForm", u"312", None))
        self.acquisitionNumberOfChannelsComboBox.setItemText(3, QCoreApplication.translate("QuattrocentoForm", u"408", None))

        self.acquisitionSamplingFrequencyComboBox.setItemText(0, QCoreApplication.translate("QuattrocentoForm", u"512", None))
        self.acquisitionSamplingFrequencyComboBox.setItemText(1, QCoreApplication.translate("QuattrocentoForm", u"2048", None))
        self.acquisitionSamplingFrequencyComboBox.setItemText(2, QCoreApplication.translate("QuattrocentoForm", u"5120", None))
        self.acquisitionSamplingFrequencyComboBox.setItemText(3, QCoreApplication.translate("QuattrocentoForm", u"10240", None))

        self.label_2.setText(QCoreApplication.translate("QuattrocentoForm", u"Number of Channels", None))
        self.label.setText(QCoreApplication.translate("QuattrocentoForm", u"Sampling Frequency", None))
        self.acquisitionDecimatorCheckBox.setText(QCoreApplication.translate("QuattrocentoForm", u"Decimator", None))
        self.acquisitionRecordingCheckBox.setText(QCoreApplication.translate("QuattrocentoForm", u"Recording", None))
        self.gridSelectionGroupBox.setTitle(QCoreApplication.translate("QuattrocentoForm", u"Grid Selection", None))
        self.gridFourCheckBox.setText(QCoreApplication.translate("QuattrocentoForm", u"Grid 4", None))
        self.gridThreeCheckBox.setText(QCoreApplication.translate("QuattrocentoForm", u"Grid 3", None))
        self.gridFiveCheckBox.setText(QCoreApplication.translate("QuattrocentoForm", u"Grid 5", None))
        self.gridSixCheckBox.setText(QCoreApplication.translate("QuattrocentoForm", u"Grid 6", None))
        self.gridTwoCheckBox.setText(QCoreApplication.translate("QuattrocentoForm", u"Grid 2", None))
        self.gridOneCheckBox.setText(QCoreApplication.translate("QuattrocentoForm", u"Grid 1", None))
        self.connectionGroupBox.setTitle(QCoreApplication.translate("QuattrocentoForm", u"Connection parameters", None))
        self.label_4.setText(QCoreApplication.translate("QuattrocentoForm", u"IP", None))
        self.connectionIPLineEdit.setText(QCoreApplication.translate("QuattrocentoForm", u"169.254.1.10", None))
        self.label_5.setText(QCoreApplication.translate("QuattrocentoForm", u"Port", None))
        self.connectionPortLineEdit.setText(QCoreApplication.translate("QuattrocentoForm", u"23456", None))
    # retranslateUi

