import sqlite3 as sql
import numpy
def data(url):
    conn = sql.connect("website.db")
    cursor = conn.cursor()
    try:
        url = str(url)
    except ValueError:
        return False
    cursor.execute("select Opt from Website where Web = " + url)
    s = cursor.fetchall()
    if(s.length != 0):
        return s[0]
    else:
        return neural(url)
def neural(url):
    return False
