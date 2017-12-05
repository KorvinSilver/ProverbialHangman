# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiLanguageSelect.ui'
#
# Created: Tue Dec  5 18:29:37 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_LanguageSelector(object):
    def setupUi(self, LanguageSelector):
        LanguageSelector.setObjectName("LanguageSelector")
        LanguageSelector.resize(300, 100)
        self.centralwidget = QtWidgets.QWidget(LanguageSelector)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.SetLanguage = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.SetLanguage.sizePolicy().hasHeightForWidth())
        self.SetLanguage.setSizePolicy(sizePolicy)
        self.SetLanguage.setObjectName("SetLanguage")
        self.horizontalLayout.addWidget(self.SetLanguage)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20,
                                            QtWidgets.QSizePolicy.Fixed,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        LanguageSelector.setCentralWidget(self.centralwidget)

        self.retranslateUi(LanguageSelector)
        QtCore.QMetaObject.connectSlotsByName(LanguageSelector)

    def retranslateUi(self, LanguageSelector):
        LanguageSelector.setWindowTitle(
            QtWidgets.QApplication.translate("LanguageSelector", "MainWindow",
                                             None, -1))
        self.SetLanguage.setText(
            QtWidgets.QApplication.translate("LanguageSelector", "OK", None,
                                             -1))
