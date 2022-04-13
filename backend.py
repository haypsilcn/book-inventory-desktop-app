import sqlite3


def connect():
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book ("
                   "id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def isFound(isbn):
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE isbn=?", (isbn,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def view():
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, year, isbn FROM book")
    rows = cursor.fetchall()
    conn.close()
    return rows

def insert(title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()

    if len(title) != 0 and len(author) == 0:  # author empty
        title = "%" + title + "%"
        cursor.execute("SELECT title, author, year, isbn FROM book WHERE title LIKE ? OR year=? OR isbn=?", (title, year, isbn))
    elif len(title) == 0 and len(author) != 0:  # title empty
        author = "%" + author + "%"
        cursor.execute("SELECT title, author, year, isbn FROM book WHERE author LIKE ? OR year=? OR isbn=?", (author, year, isbn))
    elif len(title) != 0 and len(author) != 0:
        title = "%" + title + "%"
        author = "%" + author + "%"
        cursor.execute("SELECT title, author, year, isbn FROM book WHERE title LIKE ? OR author LIKE ? OR year=? OR isbn=?", (title, author, year, isbn))
    else:  # title and author empty
        cursor.execute("SELECT title, author, year, isbn FROM book WHERE year=? OR isbn=?", (year, isbn))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete(title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM book WHERE title=? AND author=? AND year=? AND isbn=?", (title, author, year, isbn))
    conn.commit()
    conn.close()

def update(newTitle, newAuthor, newYear, isbn):
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE book SET title=?, author=?, year=? WHERE isbn=?", (newTitle, newAuthor, newYear, isbn))
    conn.commit()
    conn.close()


connect()