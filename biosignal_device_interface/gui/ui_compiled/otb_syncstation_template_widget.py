# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'otb_syncstation_template_widget.ui'
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
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QWidget)

class Ui_SyncStationForm(object):
    def setupUi(self, SyncStationForm):
        if not SyncStationForm.objectName():
            SyncStationForm.setObjectName(u"SyncStationForm")
        SyncStationForm.resize(350, 608)
        self.gridLayout = QGridLayout(SyncStationForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.inputGroupBox = QGroupBox(SyncStationForm)
        self.inputGroupBox.setObjectName(u"inputGroupBox")
        self.gridLayout_3 = QGridLayout(self.inputGroupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.inputWorkingModeComboBox = QComboBox(self.inputGroupBox)
        self.inputWorkingModeComboBox.addItem("")
        self.inputWorkingModeComboBox.addItem("")
        self.inputWorkingModeComboBox.setObjectName(u"inputWorkingModeComboBox")

        self.gridLayout_3.addWidget(self.inputWorkingModeComboBox, 0, 1, 1, 1)

        self.label_5 = QLabel(self.inputGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.probesTabWidget = QTabWidget(self.inputGroupBox)
        self.probesTabWidget.setObjectName(u"probesTabWidget")
        self.muoviWidget = QWidget()
        self.muoviWidget.setObjectName(u"muoviWidget")
        self.gridLayout_5 = QGridLayout(self.muoviWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.muoviProbeOneEnableCheckBox = QCheckBox(self.muoviWidget)
        self.muoviProbeOneEnableCheckBox.setObjectName(u"muoviProbeOneEnableCheckBox")

        self.gridLayout_5.addWidget(self.muoviProbeOneEnableCheckBox, 0, 0, 1, 1)

        self.muoviProbeOneDetectionModeComboBox = QComboBox(self.muoviWidget)
        self.muoviProbeOneDetectionModeComboBox.addItem("")
        self.muoviProbeOneDetectionModeComboBox.addItem("")
        self.muoviProbeOneDetectionModeComboBox.addItem("")
        self.muoviProbeOneDetectionModeComboBox.addItem("")
        self.muoviProbeOneDetectionModeComboBox.setObjectName(u"muoviProbeOneDetectionModeComboBox")

        self.gridLayout_5.addWidget(self.muoviProbeOneDetectionModeComboBox, 0, 1, 1, 1)

        self.muoviProbeTwoEnableCheckBox = QCheckBox(self.muoviWidget)
        self.muoviProbeTwoEnableCheckBox.setObjectName(u"muoviProbeTwoEnableCheckBox")

        self.gridLayout_5.addWidget(self.muoviProbeTwoEnableCheckBox, 1, 0, 1, 1)

        self.muoviProbeTwoDetectionModeComboBox = QComboBox(self.muoviWidget)
        self.muoviProbeTwoDetectionModeComboBox.addItem("")
        self.muoviProbeTwoDetectionModeComboBox.addItem("")
        self.muoviProbeTwoDetectionModeComboBox.addItem("")
        self.muoviProbeTwoDetectionModeComboBox.addItem("")
        self.muoviProbeTwoDetectionModeComboBox.setObjectName(u"muoviProbeTwoDetectionModeComboBox")

        self.gridLayout_5.addWidget(self.muoviProbeTwoDetectionModeComboBox, 1, 1, 1, 1)

        self.muoviProbeThreeEnableCheckBox = QCheckBox(self.muoviWidget)
        self.muoviProbeThreeEnableCheckBox.setObjectName(u"muoviProbeThreeEnableCheckBox")

        self.gridLayout_5.addWidget(self.muoviProbeThreeEnableCheckBox, 2, 0, 1, 1)

        self.muoviProbeThreeDetectionModeComboBox = QComboBox(self.muoviWidget)
        self.muoviProbeThreeDetectionModeComboBox.addItem("")
        self.muoviProbeThreeDetectionModeComboBox.addItem("")
        self.muoviProbeThreeDetectionModeComboBox.addItem("")
        self.muoviProbeThreeDetectionModeComboBox.addItem("")
        self.muoviProbeThreeDetectionModeComboBox.setObjectName(u"muoviProbeThreeDetectionModeComboBox")

        self.gridLayout_5.addWidget(self.muoviProbeThreeDetectionModeComboBox, 2, 1, 1, 1)

        self.muoviProbeFourEnableCheckBox = QCheckBox(self.muoviWidget)
        self.muoviProbeFourEnableCheckBox.setObjectName(u"muoviProbeFourEnableCheckBox")

        self.gridLayout_5.addWidget(self.muoviProbeFourEnableCheckBox, 3, 0, 1, 1)

        self.muoviProbeFourDetectionModeComboBox = QComboBox(self.muoviWidget)
        self.muoviProbeFourDetectionModeComboBox.addItem("")
        self.muoviProbeFourDetectionModeComboBox.addItem("")
        self.muoviProbeFourDetectionModeComboBox.addItem("")
        self.muoviProbeFourDetectionModeComboBox.addItem("")
        self.muoviProbeFourDetectionModeComboBox.setObjectName(u"muoviProbeFourDetectionModeComboBox")

        self.gridLayout_5.addWidget(self.muoviProbeFourDetectionModeComboBox, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 154, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.probesTabWidget.addTab(self.muoviWidget, "")
        self.muoviPlusWidget = QWidget()
        self.muoviPlusWidget.setObjectName(u"muoviPlusWidget")
        self.gridLayout_4 = QGridLayout(self.muoviPlusWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.muoviPlusProbeOneEnableCheckBox = QCheckBox(self.muoviPlusWidget)
        self.muoviPlusProbeOneEnableCheckBox.setObjectName(u"muoviPlusProbeOneEnableCheckBox")

        self.gridLayout_4.addWidget(self.muoviPlusProbeOneEnableCheckBox, 0, 0, 1, 1)

        self.muoviPlusProbeOneDetectionModeComboBox = QComboBox(self.muoviPlusWidget)
        self.muoviPlusProbeOneDetectionModeComboBox.addItem("")
        self.muoviPlusProbeOneDetectionModeComboBox.addItem("")
        self.muoviPlusProbeOneDetectionModeComboBox.addItem("")
        self.muoviPlusProbeOneDetectionModeComboBox.addItem("")
        self.muoviPlusProbeOneDetectionModeComboBox.setObjectName(u"muoviPlusProbeOneDetectionModeComboBox")

        self.gridLayout_4.addWidget(self.muoviPlusProbeOneDetectionModeComboBox, 0, 1, 1, 1)

        self.muoviPlusProbeTwoEnableCheckBox = QCheckBox(self.muoviPlusWidget)
        self.muoviPlusProbeTwoEnableCheckBox.setObjectName(u"muoviPlusProbeTwoEnableCheckBox")

        self.gridLayout_4.addWidget(self.muoviPlusProbeTwoEnableCheckBox, 1, 0, 1, 1)

        self.muoviPlusProbeTwoDetectionModeComboBox = QComboBox(self.muoviPlusWidget)
        self.muoviPlusProbeTwoDetectionModeComboBox.addItem("")
        self.muoviPlusProbeTwoDetectionModeComboBox.addItem("")
        self.muoviPlusProbeTwoDetectionModeComboBox.addItem("")
        self.muoviPlusProbeTwoDetectionModeComboBox.addItem("")
        self.muoviPlusProbeTwoDetectionModeComboBox.setObjectName(u"muoviPlusProbeTwoDetectionModeComboBox")

        self.gridLayout_4.addWidget(self.muoviPlusProbeTwoDetectionModeComboBox, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.probesTabWidget.addTab(self.muoviPlusWidget, "")
        self.duePlusWidget = QWidget()
        self.duePlusWidget.setObjectName(u"duePlusWidget")
        self.gridLayout_16 = QGridLayout(self.duePlusWidget)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.duePlusProbeNineEnableCheckBox = QCheckBox(self.duePlusWidget)
        self.duePlusProbeNineEnableCheckBox.setObjectName(u"duePlusProbeNineEnableCheckBox")

        self.gridLayout_16.addWidget(self.duePlusProbeNineEnableCheckBox, 9, 0, 1, 1)

        self.duePlusProbeTenEnableCheckBox = QCheckBox(self.duePlusWidget)
        self.duePlusProbeTenEnableCheckBox.setObjectName(u"duePlusProbeTenEnableCheckBox")

        self.gridLayout_16.addWidget(self.duePlusProbeTenEnableCheckBox, 10, 0, 1, 1)

        self.duePlusProbeSixDetectionModeComboBox = QComboBox(self.duePlusWidget)
        self.duePlusProbeSixDetectionModeComboBox.addItem("")
        self.duePlusProbeSixDetectionModeComboBox.addItem("")
        self.duePlusProbeSixDetectionModeComboBox.addItem("")
        self.duePlusProbeSixDetectionModeComboBox.addItem("")
        self.duePlusProbeSixDetectionModeComboBox.setObjectName(u"duePlusProbeSixDetectionModeComboBox")

        self.gridLayout_16.addWidget(self.duePlusProbeSixDetectionModeComboBox, 6, 2, 1, 1)

        self.duePlusProbeTenDetectionModeComboBox = QComboBox(self.duePlusWidget)
        self.duePlusProbeTenDetectionModeComboBox.addItem("")
        self.duePlusProbeTenDetectionModeComboBox.addItem("")
        self.duePlusProbeTenDetectionModeComboBox.addItem("")
        self.duePlusProbeTenDetectionModeComboBox.addItem("")
        self.duePlusProbeTenDetectionModeComboBox.setObjectName(u"duePlusProbeTenDetectionModeComboBox")

        self.gridLayout_16.addWidget(self.duePlusProbeTenDetectionModeComboBox, 10, 2, 1, 1)

        self.duePlusProbeNineDetectionModeComboBox = QComboBox(self.duePlusWidget)
        self.duePlusProbeNineDetectionModeComboBox.addItem("")
        self.duePlusProbeNineDetectionModeComboBox.addItem("")
        self.duePlusProbeNineDetectionModeComboBox.addItem("")
        self.duePlusProbeNineDetectionModeComboBox.addItem("")
        self.duePlusProbeNineDetectionModeComboBox.setObjectName(u"duePlusProbeNineDetectionModeComboBox")

        self.gridLayout_16.addWidget(self.duePlusProbeNineDetectionModeComboBox, 9, 2, 1, 1)

        self.duePlusProbeFourDetectionModeComboBox = QComboBox(self.duePlusWidget)
        self.duePlusProbeFourDetectionModeComboBox.addItem("")
        self.duePlusProbeFourDetectionModeComboBox.addItem("")
        self.duePlusProbeFourDetectionModeComboBox.addItem("")
        self.duePlusProbeFourDetectionModeComboBox.addItem("")
        self.duePlusProbeFourDetectionModeComboBox.setObjectName(u"duePlusProbeFourDetectionModeComboBox")

        self.gridLayout_16.addWidget(self.duePlusProbeFourDetectionModeComboBox, 4, 2, 1, 1)

        self.duePlusProbeThreeEnableCheckBox = QCheckBox(self.duePlusWidget)
        self.duePlusProbeThreeEnableCheckBox.setObjectName(u"duePlusProbeThreeEnableCheckBox")

        self.gridLayout_16.addWidget(self.duePlusProbeThreeEnableCheckBox, 3, 0, 1, 1)

        self.duePlusProbeSixEnableCheckBox = QCheckBox(self.duePlusWidget)
        self.duePlusProbeSixEnableCheckBox.setObjectName(u"duePlusProbeSixEnableCheckBox")

        self.gridLayout_16.addWidget(self.duePlusProbeSixEnableCheckBox, 6, 0, 1, 1)

        self.duePlusProbeEightEnableCheckBox = QCheckBox(self.duePlusWidget)
        self.duePlusProbeEightEnableCheckBox.setObjectName(u"duePlusProbeEightEnableCheckBox")

        self.gridLayout_16.addWidget(self.duePlusProbeEightEnableCheckBox, 8, 0, 1, 1)

        self.duePlusProbeThreeDetectionModeComboBox = QComboBox(self.duePlusWidget)
        self.duePlusProbeThreeDetectionModeComboBox.addItem("")
        self.duePlusProbeThreeDetectionModeComboBox.addItem("")
        self.duePlusProbeThreeDetectionModeComboBox.addItem("")
        self.duePlusProbeThreeDetectionModeComboBox.addItem("")
        self.duePlusProbeThreeDetectionModeComboBox.setObjectName(u"duePlusProbeThreeDetectionModeComboBox")

        self.gridLayout_16.addWidget(self.duePlusProbeThreeDetectionModeComboBox, 3, 2, 1, 1)

        self.duePlusProbeSevenEnableCheckBox = QCheckBox(self.duePlusWidget)
        self.duePlusProbeSevenEnableCheckBox.setObjectName(u"duePlusProbeSevenEnableCheckBox")

        self.gridLayout_16.addWidget(self.duePlusProbeSevenEnableCheckBox, 7, 0, 1, 1)

        self.duePlusProbeTwoDetectionModeComboBox = QComboBox(self.duePlusWidget)
        self.duePlusProbeTwoDetectionModeComboBox.addItem("")
        self.duePlusProbeTwoDetectionModeComboBox.addItem("")
        self.duePlusProbeTwoDetectionModeComboBox.addItem("")
        self.duePlusProbeTwoDetectionModeComboBox.addItem("")
        self.duePlusProbeTwoDetectionModeComboBox.setObjectName(u"duePlusProbeTwoDetectionModeComboBox")

        self.gridLayout_16.addWidget(self.duePlusProbeTwoDetectionModeComboBox, 2, 2, 1, 1)

        self.duePlusProbeTwoEnableCheckBox = QCheckBox(self.duePlusWidget)
        self.duePlusProbeTwoEnableCheckBox.setObjectName(u"duePlusProbeTwoEnableCheckBox")

        self.gridLayout_16.addWidget(self.duePlusProbeTwoEnableCheckBox, 2, 0, 1, 1)

        self.duePlusProbeEightDetectionModeComboBox = QComboBox(self.duePlusWidget)
        self.duePlusProbeEightDetectionModeComboBox.addItem("")
        self.duePlusProbeEightDetectionModeComboBox.addItem("")
        self.duePlusProbeEightDetectionModeComboBox.addItem("")
        self.duePlusProbeEightDetectionModeComboBox.addItem("")
        self.duePlusProbeEightDetectionModeComboBox.setObjectName(u"duePlusProbeEightDetectionModeComboBox")

        self.gridLayout_16.addWidget(self.duePlusProbeEightDetectionModeComboBox, 8, 2, 1, 1)

        self.duePlusProbeSevenDetectionModeComboBox = QComboBox(self.duePlusWidget)
        self.duePlusProbeSevenDetectionModeComboBox.addItem("")
        self.duePlusProbeSevenDetectionModeComboBox.addItem("")
        self.duePlusProbeSevenDetectionModeComboBox.addItem("")
        self.duePlusProbeSevenDetectionModeComboBox.addItem("")
        self.duePlusProbeSevenDetectionModeComboBox.setObjectName(u"duePlusProbeSevenDetectionModeComboBox")

        self.gridLayout_16.addWidget(self.duePlusProbeSevenDetectionModeComboBox, 7, 2, 1, 1)

        self.duePlusProbeFourEnableCheckBox = QCheckBox(self.duePlusWidget)
        self.duePlusProbeFourEnableCheckBox.setObjectName(u"duePlusProbeFourEnableCheckBox")

        self.gridLayout_16.addWidget(self.duePlusProbeFourEnableCheckBox, 4, 0, 1, 1)

        self.duePlusProbeFiveDetectionModeComboBox = QComboBox(self.duePlusWidget)
        self.duePlusProbeFiveDetectionModeComboBox.addItem("")
        self.duePlusProbeFiveDetectionModeComboBox.addItem("")
        self.duePlusProbeFiveDetectionModeComboBox.addItem("")
        self.duePlusProbeFiveDetectionModeComboBox.addItem("")
        self.duePlusProbeFiveDetectionModeComboBox.setObjectName(u"duePlusProbeFiveDetectionModeComboBox")

        self.gridLayout_16.addWidget(self.duePlusProbeFiveDetectionModeComboBox, 5, 2, 1, 1)

        self.duePlusProbeFiveEnableCheckBox = QCheckBox(self.duePlusWidget)
        self.duePlusProbeFiveEnableCheckBox.setObjectName(u"duePlusProbeFiveEnableCheckBox")

        self.gridLayout_16.addWidget(self.duePlusProbeFiveEnableCheckBox, 5, 0, 1, 1)

        self.duePlusProbeOneDetectionModeComboBox = QComboBox(self.duePlusWidget)
        self.duePlusProbeOneDetectionModeComboBox.addItem("")
        self.duePlusProbeOneDetectionModeComboBox.addItem("")
        self.duePlusProbeOneDetectionModeComboBox.addItem("")
        self.duePlusProbeOneDetectionModeComboBox.addItem("")
        self.duePlusProbeOneDetectionModeComboBox.setObjectName(u"duePlusProbeOneDetectionModeComboBox")

        self.gridLayout_16.addWidget(self.duePlusProbeOneDetectionModeComboBox, 0, 2, 1, 1)

        self.duePlusProbeOneEnableCheckBox = QCheckBox(self.duePlusWidget)
        self.duePlusProbeOneEnableCheckBox.setObjectName(u"duePlusProbeOneEnableCheckBox")

        self.gridLayout_16.addWidget(self.duePlusProbeOneEnableCheckBox, 0, 0, 1, 1)

        self.probesTabWidget.addTab(self.duePlusWidget, "")

        self.gridLayout_3.addWidget(self.probesTabWidget, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.inputGroupBox, 1, 0, 1, 1)

        self.commandsGroupBox = QGroupBox(SyncStationForm)
        self.commandsGroupBox.setObjectName(u"commandsGroupBox")
        self.gridLayout_10 = QGridLayout(self.commandsGroupBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.commandConnectionPushButton = QPushButton(self.commandsGroupBox)
        self.commandConnectionPushButton.setObjectName(u"commandConnectionPushButton")

        self.gridLayout_10.addWidget(self.commandConnectionPushButton, 0, 0, 1, 1)

        self.commandConfigurationPushButton = QPushButton(self.commandsGroupBox)
        self.commandConfigurationPushButton.setObjectName(u"commandConfigurationPushButton")

        self.gridLayout_10.addWidget(self.commandConfigurationPushButton, 1, 0, 1, 1)

        self.commandStreamPushButton = QPushButton(self.commandsGroupBox)
        self.commandStreamPushButton.setObjectName(u"commandStreamPushButton")

        self.gridLayout_10.addWidget(self.commandStreamPushButton, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.commandsGroupBox, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.connectionGroupBox = QGroupBox(SyncStationForm)
        self.connectionGroupBox.setObjectName(u"connectionGroupBox")
        self.gridLayout_2 = QGridLayout(self.connectionGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.connectionGroupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.connectionIPAddressLabel = QLabel(self.connectionGroupBox)
        self.connectionIPAddressLabel.setObjectName(u"connectionIPAddressLabel")

        self.gridLayout_2.addWidget(self.connectionIPAddressLabel, 0, 1, 1, 1)

        self.label_3 = QLabel(self.connectionGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.connectionPortLabel = QLabel(self.connectionGroupBox)
        self.connectionPortLabel.setObjectName(u"connectionPortLabel")

        self.gridLayout_2.addWidget(self.connectionPortLabel, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.connectionGroupBox, 0, 0, 1, 1)


        self.retranslateUi(SyncStationForm)

        self.inputWorkingModeComboBox.setCurrentIndex(1)
        self.probesTabWidget.setCurrentIndex(0)
        self.muoviProbeOneDetectionModeComboBox.setCurrentIndex(1)
        self.muoviProbeTwoDetectionModeComboBox.setCurrentIndex(1)
        self.muoviProbeThreeDetectionModeComboBox.setCurrentIndex(1)
        self.muoviProbeFourDetectionModeComboBox.setCurrentIndex(1)
        self.muoviPlusProbeOneDetectionModeComboBox.setCurrentIndex(1)
        self.muoviPlusProbeTwoDetectionModeComboBox.setCurrentIndex(1)
        self.duePlusProbeSixDetectionModeComboBox.setCurrentIndex(1)
        self.duePlusProbeTenDetectionModeComboBox.setCurrentIndex(1)
        self.duePlusProbeNineDetectionModeComboBox.setCurrentIndex(1)
        self.duePlusProbeFourDetectionModeComboBox.setCurrentIndex(1)
        self.duePlusProbeThreeDetectionModeComboBox.setCurrentIndex(1)
        self.duePlusProbeTwoDetectionModeComboBox.setCurrentIndex(1)
        self.duePlusProbeEightDetectionModeComboBox.setCurrentIndex(1)
        self.duePlusProbeSevenDetectionModeComboBox.setCurrentIndex(1)
        self.duePlusProbeFiveDetectionModeComboBox.setCurrentIndex(1)
        self.duePlusProbeOneDetectionModeComboBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SyncStationForm)
    # setupUi

    def retranslateUi(self, SyncStationForm):
        SyncStationForm.setWindowTitle(QCoreApplication.translate("SyncStationForm", u"SyncStationForm", None))
        self.inputGroupBox.setTitle(QCoreApplication.translate("SyncStationForm", u"Input Parameters", None))
        self.inputWorkingModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"EEG", None))
        self.inputWorkingModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"EMG", None))

        self.label_5.setText(QCoreApplication.translate("SyncStationForm", u"Working Mode", None))
        self.muoviProbeOneEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Muovi Probe 1", None))
        self.muoviProbeOneDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.muoviProbeOneDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.muoviProbeOneDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.muoviProbeOneDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.muoviProbeTwoEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Muovi Probe 2", None))
        self.muoviProbeTwoDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.muoviProbeTwoDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.muoviProbeTwoDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.muoviProbeTwoDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.muoviProbeThreeEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Muovi Probe 3", None))
        self.muoviProbeThreeDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.muoviProbeThreeDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.muoviProbeThreeDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.muoviProbeThreeDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.muoviProbeFourEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Muovi Probe 4", None))
        self.muoviProbeFourDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.muoviProbeFourDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.muoviProbeFourDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.muoviProbeFourDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.probesTabWidget.setTabText(self.probesTabWidget.indexOf(self.muoviWidget), QCoreApplication.translate("SyncStationForm", u"Muovi", None))
        self.muoviPlusProbeOneEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Muovi+ Probe 1", None))
        self.muoviPlusProbeOneDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.muoviPlusProbeOneDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.muoviPlusProbeOneDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.muoviPlusProbeOneDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.muoviPlusProbeTwoEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Muovi+ Probe 2", None))
        self.muoviPlusProbeTwoDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.muoviPlusProbeTwoDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.muoviPlusProbeTwoDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.muoviPlusProbeTwoDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.probesTabWidget.setTabText(self.probesTabWidget.indexOf(self.muoviPlusWidget), QCoreApplication.translate("SyncStationForm", u"Muovi+", None))
        self.duePlusProbeNineEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Due+ Probe 9", None))
        self.duePlusProbeTenEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Due+ Probe 10", None))
        self.duePlusProbeSixDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.duePlusProbeSixDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.duePlusProbeSixDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.duePlusProbeSixDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.duePlusProbeTenDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.duePlusProbeTenDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.duePlusProbeTenDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.duePlusProbeTenDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.duePlusProbeNineDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.duePlusProbeNineDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.duePlusProbeNineDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.duePlusProbeNineDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.duePlusProbeFourDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.duePlusProbeFourDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.duePlusProbeFourDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.duePlusProbeFourDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.duePlusProbeThreeEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Due+ Probe 3", None))
        self.duePlusProbeSixEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Due+ Probe 6", None))
        self.duePlusProbeEightEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Due+ Probe 8", None))
        self.duePlusProbeThreeDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.duePlusProbeThreeDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.duePlusProbeThreeDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.duePlusProbeThreeDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.duePlusProbeSevenEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Due+ Probe 7", None))
        self.duePlusProbeTwoDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.duePlusProbeTwoDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.duePlusProbeTwoDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.duePlusProbeTwoDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.duePlusProbeTwoEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Due+ Probe 2", None))
        self.duePlusProbeEightDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.duePlusProbeEightDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.duePlusProbeEightDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.duePlusProbeEightDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.duePlusProbeSevenDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.duePlusProbeSevenDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.duePlusProbeSevenDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.duePlusProbeSevenDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.duePlusProbeFourEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Due+ Probe 4", None))
        self.duePlusProbeFiveDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.duePlusProbeFiveDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.duePlusProbeFiveDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.duePlusProbeFiveDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.duePlusProbeFiveEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Due+ Probe 5", None))
        self.duePlusProbeOneDetectionModeComboBox.setItemText(0, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 8)", None))
        self.duePlusProbeOneDetectionModeComboBox.setItemText(1, QCoreApplication.translate("SyncStationForm", u"Monopolar (Gain 4)", None))
        self.duePlusProbeOneDetectionModeComboBox.setItemText(2, QCoreApplication.translate("SyncStationForm", u"Impedance Check", None))
        self.duePlusProbeOneDetectionModeComboBox.setItemText(3, QCoreApplication.translate("SyncStationForm", u"Test", None))

        self.duePlusProbeOneEnableCheckBox.setText(QCoreApplication.translate("SyncStationForm", u"Due+ Probe 1", None))
        self.probesTabWidget.setTabText(self.probesTabWidget.indexOf(self.duePlusWidget), QCoreApplication.translate("SyncStationForm", u"Due+", None))
        self.commandsGroupBox.setTitle(QCoreApplication.translate("SyncStationForm", u"Commands", None))
        self.commandConnectionPushButton.setText(QCoreApplication.translate("SyncStationForm", u"Connect", None))
        self.commandConfigurationPushButton.setText(QCoreApplication.translate("SyncStationForm", u"Configure", None))
        self.commandStreamPushButton.setText(QCoreApplication.translate("SyncStationForm", u"Stream", None))
        self.connectionGroupBox.setTitle(QCoreApplication.translate("SyncStationForm", u"Connection parameters", None))
        self.label.setText(QCoreApplication.translate("SyncStationForm", u"IP", None))
        self.connectionIPAddressLabel.setText(QCoreApplication.translate("SyncStationForm", u"192.168.76.1", None))
        self.label_3.setText(QCoreApplication.translate("SyncStationForm", u"TextLabel", None))
        self.connectionPortLabel.setText(QCoreApplication.translate("SyncStationForm", u"54320", None))
    # retranslateUi

