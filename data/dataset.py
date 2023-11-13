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
    cursorObj.execute("CREATE TABLE News(Id integer PRIMARY KEY, \
                                            Title text, Content_ text)\
                                            ")
    con.commit()
    
def insertMultipleRecords(con , recordList):
    try:
        cursor = con.cursor()
        query = "INSERT INTO News \
                        (Id, Title, Content_)\
                        VALUES (?, ?, ?)"
        cursor.executemany(query, recordList)
        con.commit()
    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table:\n", error)
