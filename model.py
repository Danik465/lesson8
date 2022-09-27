import sqlite3
from sqlite3 import Error


def connection():
    try:
        con = sqlite3.connect('main.db')
        return con
    except Error:
        print(Error)


def close_db(cur):
    cur.close()


def select_table(table):

    con = connection()
    cursor = con.cursor()

    cursor.execute(f'SELECT * FROM {table}')
    data = cursor.fetchall()

    close_db(cursor)

    return data


def insert_in_table(con, ent, table):
    cursor = con.cursor()

    cursor.execute(f'INSERT INTO {table} VALUES{ent}')
    con.commit()

    close_db(cursor)

