# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fill_appeal_statuses_Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox



class Ui_inputParamProcedureWindow(object):
    def setupUi(self, inputParamProcedureWindow):
        inputParamProcedureWindow.setObjectName("inputParamProcedureWindow")
        inputParamProcedureWindow.resize(900, 700)
        self.startLabel = QtWidgets.QLabel(inputParamProcedureWindow)
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
        self.passLabel = QtWidgets.QLabel(inputParamProcedureWindow)
        self.passLabel.setGeometry(QtCore.QRect(150, 230, 521, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.passLabel.setFont(font)
        self.passLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.passLabel.setAutoFillBackground(False)
        self.passLabel.setStyleSheet("")
        self.passLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passLabel.setWordWrap(False)
        self.passLabel.setObjectName("passLabel")
        self.levelLineEdit = QtWidgets.QLineEdit(inputParamProcedureWindow)
        self.levelLineEdit.setGeometry(QtCore.QRect(150, 290, 600, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.levelLineEdit.setFont(font)
        self.levelLineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.levelLineEdit.setTabletTracking(True)
        self.levelLineEdit.setStyleSheet("border-color: rgb(0, 85, 0);")
        self.levelLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.levelLineEdit.setObjectName("levelLineEdit")
        self.inputButton = QtWidgets.QPushButton(inputParamProcedureWindow)
        self.inputButton.setGeometry(QtCore.QRect(350, 510, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.inputButton.setFont(font)
        self.inputButton.setStyleSheet("")
        self.inputButton.setDefault(False)
        self.inputButton.setFlat(False)
        self.inputButton.setObjectName("inputButton")
        self.backButton = QtWidgets.QPushButton(inputParamProcedureWindow)
        self.backButton.setGeometry(QtCore.QRect(10, 90, 200, 50))
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

        self.backButton.clicked.connect(backWindowShow)
        self.inputButton.clicked.connect(lambda: delete_problem_type(self.levelLineEdit.text()))

        self.retranslateUi(inputParamProcedureWindow)
        QtCore.QMetaObject.connectSlotsByName(inputParamProcedureWindow)

    def retranslateUi(self, inputParamProcedureWindow):
        _translate = QtCore.QCoreApplication.translate
        inputParamProcedureWindow.setWindowTitle(_translate("inputParamProcedureWindow", "Dialog"))
        self.startLabel.setText(_translate("inputParamProcedureWindow", "Удалить тип проблемы"))
        self.passLabel.setText(_translate("inputParamProcedureWindow", "Введите тип проблемы:"))
        self.levelLineEdit.setPlaceholderText(_translate("inputParamProcedureWindow", "Пример: Нарушение пользовательского соглашения"))
        self.inputButton.setText(_translate("inputParamProcedureWindow", "Далее"))
        self.backButton.setText(_translate("inputParamProcedureWindow", "Назад"))


def backWindowShow():
    from QtWindows.menuWindows import showMenuWindow
    showMenuWindow()
    closeInputParamProcedureWindow()


def delete_problem_type(level):
    from WorkWithDB import delete_problem_type
    delete_problem_type(level)
    msgBox = QMessageBox()
    msgBox.setText("Проблема удалена")
    msgBox.exec_()
    pass

def show_delete_problem_type_Window():
    global show_delete_problem_type_Window
    show_delete_problem_type_Window = QtWidgets.QDialog()
    ui = Ui_inputParamProcedureWindow()
    ui.setupUi(show_delete_problem_type_Window)
    show_delete_problem_type_Window.show()



def closeInputParamProcedureWindow():
    show_delete_problem_type_Window.close()
