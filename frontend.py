from tkinter import *
import tkinter.font as font
import backend
import datetime
from tkinter import messagebox


currentYear = str(datetime.datetime.now().year)

#####################################################################
# Setting all commands for buttons
#####################################################################
def setFontSize(size):
    return font.Font(size=size)

def validateYearAndISBN():
    return False


def clearCommand():
    title.set('')
    author.set('')
    year.set('')
    isbn.set('')
    viewCommand()


def viewCommand():
    list_.delete(0, END)  # delete all entry before re-click the button
    for row in backend.view():
        list_.insert(END, str(row).removeprefix('(').removesuffix(")").replace("'", ""))


def searchCommand():
    result = backend.search(title.get(), author.get(), year.get(), isbn.get())
    if result == 0:
        messagebox.showerror("Error", "No book is found!")
    else:
        list_.delete(0, END)
        for row in backend.search(title.get(), author.get(), year.get(), isbn.get()):
            list_.insert(END, str(row).removeprefix('(').removesuffix(")").replace("'", ""))


def addCommand():
    if len(title.get()) != 0 and len(author.get()) != 0 and len(year.get()) != 0 and len(isbn.get()) != 0:
        if not year.get().isdigit():
            messagebox.showerror("Error", "Year entry only accepts numbers!")
        if not isbn.get().isdigit():
            messagebox.showerror("Error", "ISBN entry only accepts numbers!")
        if year.get().isdigit() and isbn.get().isdigit():
            if "1970" <= year.get() <= currentYear:  # The ISBN system began officially in year 1970
                if len(isbn.get()) == 10 or len(isbn.get()) == 13:
                    if len(isbn.get()) == 10 and year.get() >= "2007":
                        messagebox.showerror("Invalid ISBN", "Book published after 2007 must have 13 digits")
                    elif len(isbn.get()) == 13 and year.get() < "2007":
                        messagebox.showerror("Invalid ISBN", "Book published before 2007 only have 10 digits")
                    else:
                        backend.insert(title.get(), author.get(), year.get(), isbn.get())
                        clearCommand()  # after adding, clear all entries
                else:
                    messagebox.showerror("Invalid ISBN", "ISBN number has to have 10 or 13 digits")
            else:
                messagebox.showerror("Invalid Year", "Year entry must be between 1970 and " + currentYear)

    else:
        if len(title.get()) == 0:
            messagebox.showerror("Error", "Title cannot be empty!")
        if len(author.get()) == 0:
            messagebox.showerror("Error", "Author cannot be empty!")
        if len(year.get()) == 0:
            messagebox.showerror("Error", "Year cannot be empty!")
        if len(isbn.get()) == 0:
            messagebox.showerror("Error", "ISBN cannot be empty!")


#####################################################################
# Setting GUI
#####################################################################
window = Tk()
window.title("Book Inventory")
window.geometry("740x390")
window.resizable(False, False)

titleL = Label(window, text="Title", height=2, width=10, font=setFontSize(12))
titleL.grid(row=0, column=0)
title = StringVar()
titleEntry = Entry(window, width=20, textvariable=title, font=setFontSize(14))
titleEntry.grid(row=0, column=1)

authorL = Label(window, text="Author", height=2, width=10, font=setFontSize(12))
authorL.grid(row=0, column=2)
author = StringVar()
authorEntry = Entry(window, width=20, textvariable=author, font=setFontSize(14))
authorEntry.grid(row=0, column=3)

yearL = Label(window, text="Year", height=2, width=10, font=setFontSize(12))
yearL.grid(row=1, column=0)
year = StringVar()
yearEntry = Entry(window, width=20, textvariable=year, font=setFontSize(14))
yearEntry.grid(row=1, column=1)

isbnL = Label(window, text="ISBN", height=2, width=10, font=setFontSize(12))
isbnL.grid(row=1, column=2)
isbn = StringVar()
isbnEntry = Entry(window, width=20, textvariable=isbn, font=setFontSize(14))
isbnEntry.grid(row=1, column=3)

# create Frame() object to hold only the listbox and scrollbar
frame = Frame(window)
frame.grid(row=2, column=0, rowspan=7, columnspan=3, pady=10)

scrollBar = Scrollbar(frame, orient=VERTICAL, width=20)
slideBar = Scrollbar(frame, orient=HORIZONTAL, width=20)
list_ = Listbox(frame,
                yscrollcommand=scrollBar.set,
                xscrollcommand=slideBar.set,
                width=40, font=setFontSize(14),
                borderwidth=3)  # communicate back to the scrollbar
for book in backend.view():
    list_.insert(END, str(book).removeprefix('(').removesuffix(")").replace("'", ""))

scrollBar.config(command=list_.yview)  # create a scrollbar widget and set its command to the list box widget
slideBar.config(command=list_.xview)
slideBar.pack(side=BOTTOM, fill=X, expand=True, pady=10)
list_.pack(side=LEFT, fill=BOTH, expand=True, padx=15)
scrollBar.pack(side=RIGHT, fill=Y, expand=True)

viewButton = Button(window, text="View all", width=15, font=setFontSize(12), command=viewCommand)
searchButton = Button(window, text="Search entry", width=15, font=setFontSize(12), command=searchCommand)
addButton = Button(window, text="Add entry", width=15, font=setFontSize(12), command=addCommand)
updateButton = Button(window, text="Update selected", width=15, font=setFontSize(12))
deleteButton = Button(window, text="Delete selected", width=15, font=setFontSize(12))
closeButton = Button(window, text="Close", width=15, font=setFontSize(12))
clearButton = Button(window, text="Clear entry", width=15, font=setFontSize(12), command=clearCommand)
viewButton.grid(row=2, column=3)
searchButton.grid(row=3, column=3)
addButton.grid(row=4, column=3)
clearButton.grid(row=5, column=3)
updateButton.grid(row=6, column=3)
deleteButton.grid(row=7, column=3)
closeButton.grid(row=8, column=3)

window.mainloop()
