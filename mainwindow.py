# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.log_Browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.log_Browser.setGeometry(QtCore.QRect(20, 160, 501, 211))
        self.log_Browser.setObjectName("log_Browser")
        self.parse_image = QtWidgets.QPushButton(self.centralwidget)
        self.parse_image.setGeometry(QtCore.QRect(570, 260, 141, 111))
        self.parse_image.setObjectName("parse_image")
        self.clear_log = QtWidgets.QPushButton(self.centralwidget)
        self.clear_log.setGeometry(QtCore.QRect(440, 130, 75, 23))
        self.clear_log.setObjectName("clear_log")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 33, 711, 83))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.choose_ap = QtWidgets.QPushButton(self.widget)
        self.choose_ap.setObjectName("choose_ap")
        self.gridLayout.addWidget(self.choose_ap, 0, 0, 1, 1)
        self.show_ap = QtWidgets.QLineEdit(self.widget)
        self.show_ap.setObjectName("show_ap")
        self.gridLayout.addWidget(self.show_ap, 0, 1, 1, 1)
        self.choose_out = QtWidgets.QPushButton(self.widget)
        self.choose_out.setObjectName("choose_out")
        self.gridLayout.addWidget(self.choose_out, 1, 0, 1, 1)
        self.show_out = QtWidgets.QLineEdit(self.widget)
        self.show_out.setObjectName("show_out")
        self.gridLayout.addWidget(self.show_out, 1, 1, 1, 1)
        self.choose_xml = QtWidgets.QPushButton(self.widget)
        self.choose_xml.setObjectName("choose_xml")
        self.gridLayout.addWidget(self.choose_xml, 2, 0, 1, 1)
        self.show_xml = QtWidgets.QLineEdit(self.widget)
        self.show_xml.setObjectName("show_xml")
        self.gridLayout.addWidget(self.show_xml, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.parse_image.setText(_translate("MainWindow", "开始分包"))
        self.clear_log.setText(_translate("MainWindow", "清除log"))
        self.choose_ap.setText(_translate("MainWindow", "选择AP目录"))
        self.choose_out.setText(_translate("MainWindow", "选择输出目录"))
        self.choose_xml.setText(_translate("MainWindow", "选择XML"))

