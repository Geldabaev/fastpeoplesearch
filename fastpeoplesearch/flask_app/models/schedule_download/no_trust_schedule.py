import time
import urllib.request
import pandas as pd
import sqlite3
import requests
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup



def save_and_xlsx_to_sqlite3():  # запуск каждый день
    # скачать нужный файл по прямой ссылке
    urllib.request.urlretrieve("https://files.gossluzhba.gov.ru/49309a89-3c66-408c-805a-2d42b28e89c9/download/de137fd0-1436-4bd2-a67f-2ffffc8a9b5b", "flask_app/models/schedule_download/db_files/no_trust.xlsx")
    # преоброзование xlsx в sqlite3
    time.sleep(5)
    print("s 1")
    db = sqlite3.connect('flask_app/models/schedule_download/db_files/sqlite.db')
    dfs = pd.read_excel('flask_app/models/schedule_download/db_files/no_trust.xlsx', sheet_name=None)
    for table, df in dfs.items():
        print(table)
        print(type(table))
        print(len(table))
        df.to_sql('tableres', db, if_exists='replace')  # сбрасывать название таблицы в избежании совпадений
        print(f'{df} inserted successfully')


def search_in_sqlite3(fio: list = None) -> list:
    con = sqlite3.connect("flask_app/models/schedule_download/db_files/sqlite.db")
    cur = con.cursor()
    res = cur.execute("SELECT `Unnamed: 1` FROM tableres")
    res = res.fetchall()

    for i in res:
        punct = ('\n', ',', '?')
        if i != (None,):
            no_punct = ''.join([c for c in i if c not in punct])
            res = [i.split() for i in no_punct.split(',')]
            hi = 0
            for name in fio:
                for x in res[0]:
                    if name == x:
                        hi += 1
                        if hi > 2:  # если есть больше 2-х совпадений среди фио значит возможно это он
                            return ["Есть совпадение:", ' '.join(res[0])]
    return ["В базе данных нет совпадений"]
