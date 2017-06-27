# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maket.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 628)
        MainWindow.setWindowTitle("Лошадь со скальпелем")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 10, 47, 21))
        self.label.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(263, 40, 391, 541))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.settings = QtWidgets.QAction(MainWindow)
        self.settings.setObjectName("settings")
        self.actiontrse = QtWidgets.QAction(MainWindow)
        self.actiontrse.setObjectName("actiontrse")
        self.actiontrse_2 = QtWidgets.QAction(MainWindow)
        self.actiontrse_2.setObjectName("actiontrse_2")
        self.menu.addAction(self.settings)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.settings.setText(_translate("MainWindow", "Настройки"))
        self.actiontrse.setText(_translate("MainWindow", "trse"))
        self.actiontrse_2.setText(_translate("MainWindow", "trse"))

