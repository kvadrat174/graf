import sqlite3
import oauth2client
import gspread

import httplib2

from oauth2client.service_account import ServiceAccountCredentials
import datetime
import time

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)

gc = gspread.authorize(credentials)

sh = gc.open("lina")


def addUser(ids, name):
    conn = sqlite3.connect('telegrams.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    userid INT,
    fname TEXT,
    dateVeb TEXT);""")
    conn.commit()
    cur.execute(f"SELECT userid FROM users WHERE userid={ids};")
    one_result = cur.fetchone()
    # print(one_result)
    conn.commit()

    if one_result != None:
        # print('est')
        return True
    else:
        data = (ids, name)

        cur.execute("INSERT INTO users(userid, fname) VALUES(?, ?);", data)
        conn.commit()
        return False

def update_date(ids, val):
    conn = sqlite3.connect('telegrams.db')
    cur = conn.cursor()

    cur.execute("""UPDATE users SET dateVeb=? WHERE userid=?;""", (val, ids))
    #one_result = cur.fetchone()
    # print(one_result)
    conn.commit()

def get_vebinar(ids):
    conn = sqlite3.connect('telegrams.db')
    cur = conn.cursor()
    cur.execute(f'SELECT dateVeb FROM users WHERE userid={ids}')
    #one_result = cur.fetchone()
    print(one_result)
    return one_result

def getUsers():
    conn = sqlite3.connect('telegrams.db')
    cur = conn.cursor()
    cur.execute('SELECT userid FROM users')
    result = cur.fetchall()
    return result


def gSheet():
    wks = sh.worksheet("table")
    conn = sqlite3.connect('telegrams.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()
    resultCells = []
    conn.commit()

    for i in result:
        resultCells.append(i[0])
        resultCells.append(i[1])

    print(resultCells)

    length = int(len(result))
    ran = f'A1:B{length}'
    print(ran)
    cell_list = wks.range(ran)

    for cell, el in zip(cell_list, resultCells):
        cell.value = el
    print(len(cell_list))
    # Update in batch
    wks.update_cells(cell_list)

