# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appStatusesWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_appStatusesWindow(object):
    def setupUi(self, appStatusesWindow):
        appStatusesWindow.setObjectName("appStatusesWindow")
        appStatusesWindow.resize(900, 700)
        self.startLabel = QtWidgets.QLabel(appStatusesWindow)
        self.startLabel.setGeometry(QtCore.QRect(0, 0, 901, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.startLabel.setFont(font)
        self.startLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startLabel.setAutoFillBackground(False)
        self.startLabel.setStyleSheet("")
        self.startLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.startLabel.setWordWrap(False)
        self.startLabel.setObjectName("startLabel")
        self.backButton = QtWidgets.QPushButton(appStatusesWindow)
        self.backButton.setGeometry(QtCore.QRect(10, 20, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("")
        self.backButton.setDefault(False)
        self.backButton.setFlat(False)
        self.backButton.setObjectName("backButton")
        self.tableAppStatusesWidget = QtWidgets.QTableWidget(appStatusesWindow)
        self.tableAppStatusesWidget.setGeometry(QtCore.QRect(50, 190, 800, 350))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.tableAppStatusesWidget.setFont(font)
        self.tableAppStatusesWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableAppStatusesWidget.setObjectName("tableAppStatusesWidget")
        self.tableAppStatusesWidget.setColumnCount(0)
        self.tableAppStatusesWidget.setRowCount(0)

        self.backButton.clicked.connect(backWindowShow)

        from WorkWithDB import callAppStatusesInfo
        statusNameAppeal = callAppStatusesInfo()

        self.tableAppStatusesWidget.setRowCount(len(statusNameAppeal))
        self.tableAppStatusesWidget.setColumnCount(1)
        self.tableAppStatusesWidget.setHorizontalHeaderLabels(('Статус', ''))
        self.tableAppStatusesWidget.setColumnWidth(0, 800)

        for i in range(len(statusNameAppeal)):
            self.tableAppStatusesWidget.setItem(i, 0, QTableWidgetItem(str(statusNameAppeal[i][0])))

        self.retranslateUi(appStatusesWindow)
        QtCore.QMetaObject.connectSlotsByName(appStatusesWindow)

    def retranslateUi(self, appStatusesWindow):
        _translate = QtCore.QCoreApplication.translate
        appStatusesWindow.setWindowTitle(_translate("appStatusesWindow", "Dialog"))
        self.startLabel.setText(_translate("appStatusesWindow", "Статус приложения"))
        self.backButton.setText(_translate("appStatusesWindow", "Назад"))


def backWindowShow():
    from QtWindows.menuWindows import showMenuWindow
    showMenuWindow()
    closeAppStatusesWindow()


def showAppStatusesWindow():
    global appStatusesWindow
    appStatusesWindow = QtWidgets.QDialog()
    ui = Ui_appStatusesWindow()
    ui.setupUi(appStatusesWindow)
    appStatusesWindow.show()


def closeAppStatusesWindow():
    appStatusesWindow.close()
