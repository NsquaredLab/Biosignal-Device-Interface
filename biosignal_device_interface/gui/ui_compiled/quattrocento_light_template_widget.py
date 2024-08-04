# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quattrocento_light_template_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_QuattrocentoLightForm(object):
    def setupUi(self, QuattrocentoLightForm):
        if not QuattrocentoLightForm.objectName():
            QuattrocentoLightForm.setObjectName(u"QuattrocentoLightForm")
        QuattrocentoLightForm.resize(400, 422)
        self.gridLayout_2 = QGridLayout(QuattrocentoLightForm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(QuattrocentoLightForm)
        self.widget.setObjectName(u"widget")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.commandsGroupBox = QGroupBox(self.widget)
        self.commandsGroupBox.setObjectName(u"commandsGroupBox")
        self.gridLayout_3 = QGridLayout(self.commandsGroupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.commandConnectionPushButton = QPushButton(self.commandsGroupBox)
        self.commandConnectionPushButton.setObjectName(u"commandConnectionPushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandConnectionPushButton.sizePolicy().hasHeightForWidth())
        self.commandConnectionPushButton.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.commandConnectionPushButton, 0, 0, 2, 1)

        self.commandConfigurationPushButton = QPushButton(self.commandsGroupBox)
        self.commandConfigurationPushButton.setObjectName(u"commandConfigurationPushButton")
        sizePolicy.setHeightForWidth(self.commandConfigurationPushButton.sizePolicy().hasHeightForWidth())
        self.commandConfigurationPushButton.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.commandConfigurationPushButton, 2, 0, 1, 1)

        self.commandStreamPushButton = QPushButton(self.commandsGroupBox)
        self.commandStreamPushButton.setObjectName(u"commandStreamPushButton")
        sizePolicy.setHeightForWidth(self.commandStreamPushButton.sizePolicy().hasHeightForWidth())
        self.commandStreamPushButton.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.commandStreamPushButton, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.commandsGroupBox, 3, 0, 1, 1)

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
        self.gridTwoCheckBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_5.addWidget(self.gridTwoCheckBox, 0, 3, 1, 1)

        self.gridOneCheckBox = QCheckBox(self.gridSelectionGroupBox)
        self.gridOneCheckBox.setObjectName(u"gridOneCheckBox")

        self.gridLayout_5.addWidget(self.gridOneCheckBox, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.gridSelectionGroupBox, 2, 0, 1, 1)

        self.acquisitionGroupBox = QGroupBox(self.widget)
        self.acquisitionGroupBox.setObjectName(u"acquisitionGroupBox")
        self.gridLayout = QGridLayout(self.acquisitionGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.acquisitionSamplingFrequencyComboBox = QComboBox(self.acquisitionGroupBox)
        self.acquisitionSamplingFrequencyComboBox.addItem("")
        self.acquisitionSamplingFrequencyComboBox.addItem("")
        self.acquisitionSamplingFrequencyComboBox.addItem("")
        self.acquisitionSamplingFrequencyComboBox.addItem("")
        self.acquisitionSamplingFrequencyComboBox.setObjectName(u"acquisitionSamplingFrequencyComboBox")

        self.gridLayout.addWidget(self.acquisitionSamplingFrequencyComboBox, 0, 1, 1, 1)

        self.acquisitionStreamingFrequencyComboBox = QComboBox(self.acquisitionGroupBox)
        self.acquisitionStreamingFrequencyComboBox.addItem("")
        self.acquisitionStreamingFrequencyComboBox.addItem("")
        self.acquisitionStreamingFrequencyComboBox.addItem("")
        self.acquisitionStreamingFrequencyComboBox.addItem("")
        self.acquisitionStreamingFrequencyComboBox.addItem("")
        self.acquisitionStreamingFrequencyComboBox.addItem("")
        self.acquisitionStreamingFrequencyComboBox.setObjectName(u"acquisitionStreamingFrequencyComboBox")

        self.gridLayout.addWidget(self.acquisitionStreamingFrequencyComboBox, 1, 1, 1, 1)

        self.label_2 = QLabel(self.acquisitionGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.acquisitionGroupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.acquisitionGroupBox, 1, 0, 1, 1)

        self.connectionGroupBox = QGroupBox(self.widget)
        self.connectionGroupBox.setObjectName(u"connectionGroupBox")
        self.gridLayout_7 = QGridLayout(self.connectionGroupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_4 = QLabel(self.connectionGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.connectionGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 1, 0, 1, 1)

        self.connectionIPLabel = QLabel(self.connectionGroupBox)
        self.connectionIPLabel.setObjectName(u"connectionIPLabel")

        self.gridLayout_7.addWidget(self.connectionIPLabel, 0, 1, 1, 1)

        self.connectionPortLabel = QLabel(self.connectionGroupBox)
        self.connectionPortLabel.setObjectName(u"connectionPortLabel")

        self.gridLayout_7.addWidget(self.connectionPortLabel, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.connectionGroupBox, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.retranslateUi(QuattrocentoLightForm)

        self.acquisitionSamplingFrequencyComboBox.setCurrentIndex(1)
        self.acquisitionStreamingFrequencyComboBox.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(QuattrocentoLightForm)
    # setupUi

    def retranslateUi(self, QuattrocentoLightForm):
        QuattrocentoLightForm.setWindowTitle(QCoreApplication.translate("QuattrocentoLightForm", u"Form", None))
        self.commandsGroupBox.setTitle(QCoreApplication.translate("QuattrocentoLightForm", u"Commands", None))
        self.commandConnectionPushButton.setText(QCoreApplication.translate("QuattrocentoLightForm", u"Connect", None))
        self.commandConfigurationPushButton.setText(QCoreApplication.translate("QuattrocentoLightForm", u"Configure", None))
        self.commandStreamPushButton.setText(QCoreApplication.translate("QuattrocentoLightForm", u"Stream", None))
        self.gridSelectionGroupBox.setTitle(QCoreApplication.translate("QuattrocentoLightForm", u"Grid Selection", None))
        self.gridFourCheckBox.setText(QCoreApplication.translate("QuattrocentoLightForm", u"Grid 4", None))
        self.gridThreeCheckBox.setText(QCoreApplication.translate("QuattrocentoLightForm", u"Grid 3", None))
        self.gridFiveCheckBox.setText(QCoreApplication.translate("QuattrocentoLightForm", u"Grid 5", None))
        self.gridSixCheckBox.setText(QCoreApplication.translate("QuattrocentoLightForm", u"Grid 6", None))
        self.gridTwoCheckBox.setText(QCoreApplication.translate("QuattrocentoLightForm", u"Grid 2", None))
        self.gridOneCheckBox.setText(QCoreApplication.translate("QuattrocentoLightForm", u"Grid 1", None))
        self.acquisitionGroupBox.setTitle(QCoreApplication.translate("QuattrocentoLightForm", u"Acquisiton Parameters", None))
        self.acquisitionSamplingFrequencyComboBox.setItemText(0, QCoreApplication.translate("QuattrocentoLightForm", u"512", None))
        self.acquisitionSamplingFrequencyComboBox.setItemText(1, QCoreApplication.translate("QuattrocentoLightForm", u"2048", None))
        self.acquisitionSamplingFrequencyComboBox.setItemText(2, QCoreApplication.translate("QuattrocentoLightForm", u"5120", None))
        self.acquisitionSamplingFrequencyComboBox.setItemText(3, QCoreApplication.translate("QuattrocentoLightForm", u"10240", None))

        self.acquisitionStreamingFrequencyComboBox.setItemText(0, QCoreApplication.translate("QuattrocentoLightForm", u"1", None))
        self.acquisitionStreamingFrequencyComboBox.setItemText(1, QCoreApplication.translate("QuattrocentoLightForm", u"2", None))
        self.acquisitionStreamingFrequencyComboBox.setItemText(2, QCoreApplication.translate("QuattrocentoLightForm", u"4", None))
        self.acquisitionStreamingFrequencyComboBox.setItemText(3, QCoreApplication.translate("QuattrocentoLightForm", u"8", None))
        self.acquisitionStreamingFrequencyComboBox.setItemText(4, QCoreApplication.translate("QuattrocentoLightForm", u"16", None))
        self.acquisitionStreamingFrequencyComboBox.setItemText(5, QCoreApplication.translate("QuattrocentoLightForm", u"32", None))

        self.label_2.setText(QCoreApplication.translate("QuattrocentoLightForm", u"Streaming Frequency", None))
        self.label.setText(QCoreApplication.translate("QuattrocentoLightForm", u"Sampling Frequency", None))
        self.connectionGroupBox.setTitle(QCoreApplication.translate("QuattrocentoLightForm", u"Connection parameters", None))
        self.label_4.setText(QCoreApplication.translate("QuattrocentoLightForm", u"IP", None))
        self.label_5.setText(QCoreApplication.translate("QuattrocentoLightForm", u"Port", None))
        self.connectionIPLabel.setText(QCoreApplication.translate("QuattrocentoLightForm", u"127.0.0.1", None))
        self.connectionPortLabel.setText(QCoreApplication.translate("QuattrocentoLightForm", u"31000", None))
    # retranslateUi

