# in the name of Allah

import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('palestine_news.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE News(Scraping_ID integer PRIMARY KEY, \
                                            Group_ text, Author_ID text,\
                                            Content text, Date datetime ,Message_ID text \
                                            ,Author text ,Views text,Reactions text, \
                                            Shares text,Media text ,Comments text)")
    con.commit()
    
def insertMultipleRecords(con , recordList):
    try:
        cursor = con.cursor()

        query = "INSERT INTO News \
                        (Scraping_ID, Group_, Author_ID, Content, Date,Message_ID,\
                        Author, Views , Reactions , Shares , Media , Comments) \
                        VALUES (?, ?, ?, ?, ?)"

        cursor.executemany(query, recordList)
        con.commit()
    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table:\n", error)
