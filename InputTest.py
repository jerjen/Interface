from PyQt5.QtWidgets import QMessageBox
import re

from WorkWithDB import findWorkers, fillWorkers


def authorizationParamTest(login, password):
    if len(login) > 0:
        if re.search(str("^[a-zA-Z0-9_]{3,50}$"), login):
            if len(password) > 0:
                idWorker = findWorkers(login, password)
                if idWorker is not None:
                    from QtWindows.authorizationWindow import closeMainWindow
                    closeMainWindow()
                    from QtWindows.menuWindows import showMenuWindow
                    showMenuWindow()
                else:
                    showErrMsg("Ошибка!", "Пользователя с такими данными не найдено")
            else:
                showErrMsg("Ошибка!", "Пароль не может быть пустым")
        else:
            showErrMsg("Ошибка!", "Логин может содержать только латинские буквы, цифры и знак подчеркивания")
    else:
        showErrMsg("Ошибка!", "Логин не может быть пустым")


def registrationParamTest(lastName, firstName, login, password):
    if len(lastName) > 0:
        if re.match(str("^[а-яА-ЯёЁa-zA-Z]{3,100}$"), lastName):
            if len(firstName) > 0:
                if re.match(str("^[а-яА-ЯёЁa-zA-Z]{3,100}$"), firstName):
                    if len(login) > 0:
                        if re.search(str("^[a-zA-Z0-9_]{3,50}$"), login):
                            if len(password) > 0:
                                if re.search(str("^[a-zA-Z0-9_()-+=!@#№$%]{3,50}$"), password):
                                    fillWorkers(lastName, firstName, login, password)
                                    from QtWindows.registrationWindow import closeRegistrationWindow
                                    closeRegistrationWindow()
                                    from QtWindows.authorizationWindow import showAuthorizationWindow
                                    showAuthorizationWindow()
                                    showErrMsg("Успех!", "Вы успешно зарегистрировались")
                                else:
                                    showErrMsg("Ошибка!", "Пароль может содержать только латинские буквы, цифры и "
                                                          "специальные символы")
                            else:
                                showErrMsg("Ошибка!", "Пароль не может быть пустым")
                        else:
                            showErrMsg("Ошибка!",
                                       "Логин может содержать только латинские буквы, цифры и знак подчеркивания")
                    else:
                        showErrMsg("Ошибка!", "Логин не может быть пустым")
                else:
                    showErrMsg("Ошибка!", "Имя может содержать только буквы")
            else:
                showErrMsg("Ошибка!", "Имя не может быть пустым")
        else:
            showErrMsg("Ошибка!", "Фамилия может содержать только буквы")
    else:
        showErrMsg("Ошибка!", "Фамилия не может быть пустой")


def showErrMsg(title, errMsg):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(errMsg)
    msg.setIcon(QMessageBox.Warning)
    msg.exec_()
