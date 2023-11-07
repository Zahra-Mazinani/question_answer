import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('question_answer.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE QA(id integer PRIMARY KEY, \
                                            content text, questions text,\
                                            answer text)")
    con.commit()


con = sql_connection()

sql_table(con)