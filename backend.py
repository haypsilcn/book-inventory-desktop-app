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
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cursor.fetchall()
    conn.close()
    if len(rows) == 0:
        print("No book is found!")
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

# insert("One Last Hope", "Anne Hardy", 2018, 4836746592)
# insert("Survive", "Arthur Smith", 2000, 1479284948)
print(delete(3))
print(view())
