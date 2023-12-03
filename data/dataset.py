# in the name of Allah

import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('news.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE News2(Id integer PRIMARY KEY, \
                                            Title text, Content_ text , Date text)\
                                            ")
    con.commit()
    
def insertMultipleRecords(con , recordList):
    try:
        cursor = con.cursor()
        query = "INSERT INTO News2 \
                        (Id, Title, Content_,Date)\
                        VALUES (?, ?, ?,?)"
        cursor.executemany(query, recordList)
        con.commit()
    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table:\n", error)
