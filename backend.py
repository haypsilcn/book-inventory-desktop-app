import sqlite3


def connect():
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book ("
                   "id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


def select(isbn):
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE isbn=?", (isbn,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def view():
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    conn.close()
    return rows


def insert(title, author, year, isbn):
    if len(select(isbn)) > 0:
        print("The book with ISBN = " + str(isbn) + " is already exists!")
        print(select(isbn))
    else:
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
        cursor.execute("SELECT * FROM book WHERE title LIKE ? OR year=? OR isbn=?", (title, year, isbn))
    elif len(title) == 0 and len(author) != 0:  # title empty
        author = "%" + author + "%"
        cursor.execute("SELECT * FROM book WHERE author LIKE ? OR year=? OR isbn=?", (author, year, isbn))
    elif len(title) != 0 and len(author) != 0:
        title = "%" + title + "%"
        author = "%" + author + "%"
        cursor.execute("SELECT * FROM book WHERE title LIKE ? OR author LIKE ? OR year=? OR isbn=?", (title, author, year, isbn))
    else:  # title and author empty
        cursor.execute("SELECT * FROM book WHERE year=? OR isbn=?", (year, isbn))
    rows = cursor.fetchall()
    conn.close()
    if len(rows) == 0:
        return 0
    else:
        return rows


def delete(id):
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, newTitle, newAuthor, newYear, newISBN):
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (id, newTitle, newAuthor, newYear, newISBN))
    conn.commit()
    conn.close()


connect()

# print(type(search("", "", "2002", "")))
# result = search("", "", "2007", "")
# print(result)
