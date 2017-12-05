# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiMain.ui'
#
# Created: Tue Dec  5 18:29:56 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.CentralWidget = QtWidgets.QWidget(MainWindow)
        self.CentralWidget.setMinimumSize(QtCore.QSize(400, 400))
        self.CentralWidget.setObjectName("CentralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.CentralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.GridLayout = QtWidgets.QGridLayout()
        self.GridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.GridLayout.setSpacing(8)
        self.GridLayout.setObjectName("GridLayout")
        self.ImageLabel = QtWidgets.QLabel(self.CentralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ImageLabel.sizePolicy().hasHeightForWidth())
        self.ImageLabel.setSizePolicy(sizePolicy)
        self.ImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ImageLabel.setObjectName("ImageLabel")
        self.GridLayout.addWidget(self.ImageLabel, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.ToolButton = QtWidgets.QPushButton(self.CentralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ToolButton.sizePolicy().hasHeightForWidth())
        self.ToolButton.setSizePolicy(sizePolicy)
        self.ToolButton.setMinimumSize(QtCore.QSize(24, 24))
        self.ToolButton.setMaximumSize(QtCore.QSize(24, 24))
        self.ToolButton.setText("")
        self.ToolButton.setObjectName("ToolButton")
        self.horizontalLayout_3.addWidget(self.ToolButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Preferred,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.GuessLabel = QtWidgets.QLabel(self.CentralWidget)
        self.GuessLabel.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.GuessLabel.setObjectName("GuessLabel")
        self.verticalLayout_2.addWidget(self.GuessLabel)
        self.GuessText = QtWidgets.QLabel(self.CentralWidget)
        self.GuessText.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.GuessText.setObjectName("GuessText")
        self.verticalLayout_2.addWidget(self.GuessText)
        self.GridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.GridLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ProverbLabel = QtWidgets.QLabel(self.CentralWidget)
        self.ProverbLabel.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.ProverbLabel.setMargin(0)
        self.ProverbLabel.setIndent(-1)
        self.ProverbLabel.setObjectName("ProverbLabel")
        self.verticalLayout_3.addWidget(self.ProverbLabel)
        self.ProverbText = QtWidgets.QLabel(self.CentralWidget)
        self.ProverbText.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.ProverbText.setObjectName("ProverbText")
        self.verticalLayout_3.addWidget(self.ProverbText)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.PlayerInput = QtWidgets.QLineEdit(self.CentralWidget)
        self.PlayerInput.setInputMask("")
        self.PlayerInput.setObjectName("PlayerInput")
        self.horizontalLayout_4.addWidget(self.PlayerInput)
        self.OkButton = QtWidgets.QPushButton(self.CentralWidget)
        self.OkButton.setObjectName("OkButton")
        self.horizontalLayout_4.addWidget(self.OkButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.NewGameButton = QtWidgets.QPushButton(self.CentralWidget)
        self.NewGameButton.setObjectName("NewGameButton")
        self.horizontalLayout.addWidget(self.NewGameButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.ExitButton = QtWidgets.QPushButton(self.CentralWidget)
        self.ExitButton.setObjectName("ExitButton")
        self.horizontalLayout.addWidget(self.ExitButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 4,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem8)
        MainWindow.setCentralWidget(self.CentralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QtWidgets.QApplication.translate("MainWindow", "MainWindow", None,
                                             -1))
        self.ImageLabel.setText(
            QtWidgets.QApplication.translate("MainWindow", "ImageLabel", None,
                                             -1))
        self.GuessLabel.setText(
            QtWidgets.QApplication.translate("MainWindow", "GuessLabel", None,
                                             -1))
        self.GuessText.setText(
            QtWidgets.QApplication.translate("MainWindow", "GuessText", None,
                                             -1))
        self.ProverbLabel.setText(
            QtWidgets.QApplication.translate("MainWindow", "ProverbLabel",
                                             None, -1))
        self.ProverbText.setText(
            QtWidgets.QApplication.translate("MainWindow", "ProverbText", None,
                                             -1))
        self.OkButton.setText(
            QtWidgets.QApplication.translate("MainWindow", "OK", None, -1))
        self.NewGameButton.setText(
            QtWidgets.QApplication.translate("MainWindow", "New Game", None,
                                             -1))
        self.ExitButton.setText(
            QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
