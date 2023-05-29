import psycopg2
from datetime import datetime


"""
Класс предназначен для подключения и работы с базой данных
"""


def connectToDB():
    con = psycopg2.connect(
        database="Pochta",
        user="postgres",
        password="qwer",
        host="127.0.0.1"
    )
    return con

def fill_appeal_statuses(a):
    con = connectToDB()
    cur = con.cursor()
    cur.execute('CALL fill_appeal_statuses(%s)', (a,))
    con.commit()
    con.close()

def fill_app_statuses(a):
    con = connectToDB()
    cur = con.cursor()
    cur.execute('CALL fill_app_statuses(%s)', (a,))
    con.commit()
    con.close()

def delete_appeal_statuses(a):
    con = connectToDB()
    cur = con.cursor()
    cur.execute('CALL delete_appeal_status(%s)', (a,))
    con.commit()
    con.close()

def delete_app_statuses(a):
    con = connectToDB()
    cur = con.cursor()
    cur.execute('CALL delete_app_status(%s)', (a,))
    con.commit()
    con.close()

def delete_problem_type(a):
    con = connectToDB()
    cur = con.cursor()
    cur.execute('CALL delete_problem_type(%s)', (a,))
    con.commit()
    con.close()

def fill_certification_level(a,b):
    con = connectToDB()
    cur = con.cursor()
    cur.execute('CALL fill_certification_level(%s, %s)', (a,b))
    con.commit()
    con.close()

def fill_problem_types(a,b):
    con = connectToDB()
    cur = con.cursor()
    cur.execute('CALL fill_problem_types(%s, %s)', (a,b))
    con.commit()
    con.close()

def callCertificationLevelsInfo():
    con = connectToDB()
    cur = con.cursor()
    cur.callproc('certification_levels_info', ())
    result = cur.fetchall()
    con.close()
    return result


def callAppealStatusesInfo():
    con = connectToDB()
    cur = con.cursor()
    cur.callproc('appeal_statuses_info', ())
    result = cur.fetchall()
    con.close()
    return result

def callAppStatusesInfo():
    con = connectToDB()
    cur = con.cursor()
    cur.callproc('app_statuses_info', ())
    result = cur.fetchall()
    con.close()
    return result

def findWorkers(login, password):
    con = connectToDB()
    cur = con.cursor()
    cur.execute(
        f"SELECT w_id FROM workers WHERE w_login = '{login}' AND w_password = '{password}'")
    result = cur.fetchall()
    con.close()
    for row in result:
        if row is not None:
            return row
        else:
            return None


def fillWorkers(lastName, firstName, login, password):
    con = connectToDB()
    cur = con.cursor()
    cur.execute("INSERT INTO workers (w_first_name, w_last_name, w_login, w_password) VALUES "
                f"('{lastName}', '{firstName}', '{login}', '{password}')")
    con.commit()
    con.close()


