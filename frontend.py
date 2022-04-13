from tkinter import *
import tkinter.font as font
import backend
import datetime
import string
from tkinter import messagebox


currentYear = str(datetime.datetime.now().year)

#####################################################################
# Preparation for all below command defs
#####################################################################
def setFontSize(size):
    return font.Font(size=size)

# remove:
# - all white space from the beginning and the end
# - duplicated space between words
def removeDuplicatedSpace():
    title.set(" ".join(title.get().split()))
    author.set(" ".join(author.get().split()))
    year.set(year.get().replace(" ", ""))
    isbn.set(isbn.get().replace(" ", ""))

def validateEntries():
    if len(title.get().replace(" ", "")) == 0 and len(author.get().replace(" ", "")) == 0 and len(year.get().replace(" ", "")) == 0 and len(isbn.get().replace(" ", "")) == 0:
        messagebox.showerror("Empty Entries", "Cannot execute due to all entries are empty")
    elif len(title.get().replace(" ", "")) != 0 and len(author.get().replace(" ", "")) != 0 and len(year.get().replace(" ", "")) != 0 and len(isbn.get().replace(" ", "")) != 0:
        if title.get().replace(" ", "").isalnum():
            if author.get().replace(" ", "").isalnum():
                if not year.get().replace(" ", "").isdigit() and not isbn.get().replace(" ", "").isdigit():
                    messagebox.showerror("Invalid Entries", "Year and ISBN entries only accept digits")
                elif year.get().replace(" ", "").isdigit() and not isbn.get().replace(" ", "").isdigit():
                    messagebox.showerror("Invalid Entry", "ISBN entry only accepts numbers")
                elif not year.get().replace(" ", "").isdigit() and isbn.get().replace(" ", "").isdigit():
                    messagebox.showerror("Invalid Entry", "Year entry only accepts numbers")
                else:  # year and isbn both are digits
                    # if len(year.get().replace(" ", "")) == 4:
                    if len(year.get().replace(" ", "")) == 4 and "1970" <= year.get().replace(" ", "") <= currentYear:  # The ISBN system began officially in year 1970
                        if len(isbn.get().replace(" ", "")) == 10 or len(isbn.get().replace(" ", "")) == 13:
                            if len(isbn.get().replace(" ", "")) == 10 and currentYear >= year.get().replace(" ", "") >= "2007":
                                messagebox.showerror("Invalid ISBN", "Book published after 2007 must have 13 digits")
                            elif len(isbn.get().replace(" ", "")) == 13 and "1970" <= year.get().replace(" ", "") < "2007":
                                messagebox.showerror("Invalid ISBN", "Book published before 2007 only have 10 digits")
                            else:
                                return True
                        else:
                            messagebox.showerror("Invalid ISBN", "ISBN number has to have 10 digits for books published BEFORE 2007 "
                                                                 "and 13 digits for books published AFTER 2007")
                    else:
                        if len(isbn.get().replace(" ", "")) == 10 or len(isbn.get().replace(" ", "")) == 13:
                            messagebox.showerror("Invalid Year", "Year entry must be between 1970 and " + currentYear)
                        else:
                            messagebox.showerror("Invalid Year and ISBN", "Year entry must be between 1970 and " + currentYear
                                                 + "\nISBN number has to have 10 digits for books published BEFORE 2007 "
                                                   "and 13 digits for books published AFTER 2007")
            else:  # title isalnum && not author isalnum
                if not year.get().replace(" ", "").isdigit() and not isbn.get().replace(" ", "").isdigit():
                    messagebox.showerror("Invalid Entries", "Author entry only accepts letters and digits\nYear and ISBN entries only accept digits")
                elif year.get().replace(" ", "").isdigit() and not isbn.get().replace(" ", "").isdigit():
                    messagebox.showerror("Invalid Entries", "Author entry only accepts letters and digits\nISBN entry only accepts numbers")
                elif not year.get().replace(" ", "").isdigit() and isbn.get().replace(" ", "").isdigit():
                    messagebox.showerror("Invalid Entries", "Author entry only accepts letters and digits\nYear entry only accepts numbers")
                else:  # year and isbn both are digits
                    if len(year.get().replace(" ", "")) == 4 and "1970" <= year.get().replace(" ", "") <= currentYear:  # The ISBN system began officially in year 1970
                        if len(isbn.get().replace(" ", "")) == 10 or len(isbn.get().replace(" ", "")) == 13:
                            if len(isbn.get().replace(" ", "")) == 10 and year.get().replace(" ", "") >= "2007":
                                messagebox.showerror("Invalid Entries", "Author entry only accepts letters and digits\nBook published after 2007 must have 13 digits")
                            elif len(isbn.get().replace(" ", "")) == 13 and year.get().replace(" ", "") < "2007":
                                messagebox.showerror("Invalid Entries", "Author entry only accepts letters and digits\nBook published before 2007 only have 10 digits")
                            else:
                                messagebox.showerror("Invalid Author", "Author entry only accepts letters and digits")
                        else:
                            messagebox.showerror("Invalid Entries", "Author entry only accepts letters and digits\nISBN number has to have 10 or 13 digits")
                    else:
                        if len(isbn.get().replace(" ", "")) == 10 or len(isbn.get().replace(" ", "")) == 13:
                            messagebox.showerror("Invalid Entries", "Author entry only accepts letters and digits\nYear entry must be between 1970 and " + currentYear)
                        else:
                            messagebox.showerror("Invalid Entries", "Author entry only accepts letters and digits\nYear entry must be between 1970 and " + currentYear
                                                 + "\nISBN number has to have 10 digits for books published BEFORE 2007 "
                                                   "and 13 digits for books published AFTER 2007")
        else:  # title not isalnum
            if author.get().replace(" ", "").isalnum():
                if not year.get().replace(" ", "").isdigit() and not isbn.get().replace(" ", "").isdigit():
                    messagebox.showerror("Invalid Entries", "Title entry only accepts letters and digits\nYear and ISBN entries only accept digits")
                elif year.get().replace(" ", "").isdigit() and not isbn.get().replace(" ", "").isdigit():
                    messagebox.showerror("Invalid Entry", "Title entry only accepts letters and digits\nISBN entry only accepts numbers")
                elif not year.get().replace(" ", "").isdigit() and isbn.get().replace(" ", "").isdigit():
                    messagebox.showerror("Invalid Entry", "Title entry only accepts letters and digits\nYear entry only accepts numbers")
                else:  # year and isbn both are digits
                    if len(year.get().replace(" ", "")) == 4 and "1970" <= year.get().replace(" ", "") <= currentYear:  # The ISBN system began officially in year 1970
                        if len(isbn.get().replace(" ", "")) == 10 or len(isbn.get().replace(" ", "")) == 13:
                            if len(isbn.get().replace(" ", "")) == 10 and year.get().replace(" ", "") >= "2007":
                                messagebox.showerror("Invalid Title and ISBN", "Title entry only accepts letters and digits\nBook published after 2007 must have 13 digits")
                            elif len(isbn.get().replace(" ", "")) == 13 and year.get().replace(" ", "") < "2007":
                                messagebox.showerror("Invalid Title and ISBN", "Title entry only accepts letters and digits\nBook published before 2007 only have 10 digits")
                            else:
                                messagebox.showerror("Invalid Title", "Title entry only accepts letters and digits")
                        else:
                            messagebox.showerror("Invalid Title and ISBN", "Title entry only accepts letters and digits\n"
                                                                           "ISBN number has to have 10 digits for books published BEFORE 2007 "
                                                                           "and 13 digits for books published AFTER 2007")
                    else:
                        if len(isbn.get().replace(" ", "")) == 10 or len(isbn.get().replace(" ", "")) == 13:
                            messagebox.showerror("Invalid Title and Year", "Title entry only accepts letters and digits\nYear entry must be between 1970 and " + currentYear)
                        else:
                            messagebox.showerror("Invalid Entries", "Title entry only accepts letters and digits\nYear entry must be between 1970 and " + currentYear
                                                 + "\nISBN number has to have 10 digits for books published BEFORE 2007 "
                                                   "and 13 digits for books published AFTER 2007")
            else:  # title not isalnum && not author isalnum
                if not year.get().replace(" ", "").isdigit() and not isbn.get().replace(" ", "").isdigit():
                    messagebox.showerror("Invalid Entries", "Title and Author entries only accept letters and digits\nYear and ISBN entries only accept digits")
                elif year.get().replace(" ", "").isdigit() and not isbn.get().replace(" ", "").isdigit():
                    messagebox.showerror("Invalid Entries", "Title and Author entries only accept letters and digits\nISBN entry only accepts numbers")
                elif not year.get().replace(" ", "").isdigit() and isbn.get().replace(" ", "").isdigit():
                    messagebox.showerror("Invalid Entries", "Title and Author entries only accept letters and digits\nYear entry only accepts numbers")
                else:  # year and isbn both are digits
                    if len(year.get().replace(" ", "")) == 4 and "1970" <= year.get().replace(" ", "") <= currentYear:  # The ISBN system began officially in year 1970
                        if len(isbn.get().replace(" ", "")) == 10 or len(isbn.get().replace(" ", "")) == 13:
                            if len(isbn.get().replace(" ", "")) == 10 and year.get().replace(" ", "") >= "2007":
                                messagebox.showerror("Invalid Entries", "Title and Author entries only accept letters and digits\nBook published after 2007 must have 13 digits")
                            elif len(isbn.get().replace(" ", "")) == 13 and year.get().replace(" ", "") < "2007":
                                messagebox.showerror("Invalid Entries", "Title and Author entries only accept letters and digits\nBook published before 2007 only have 10 digits")
                            else:
                                messagebox.showerror("Invalid Title and Author", "Title and Author entries only accept letters and digits\n")
                        else:
                            messagebox.showerror("Invalid Entries", "Title and Author entries only accept letters and digits"
                                                                    "\nISBN number has to have 10 digits for books published BEFORE 2007 "
                                                                    "and 13 digits for books published AFTER 2007")
                    else:
                        if len(isbn.get().replace(" ", "")) == 10 or len(isbn.get().replace(" ", "")) == 13:
                            messagebox.showerror("Invalid Entries", "Title and Author entries only accept letters and digits\nYear entry must be between 1970 and " + currentYear)
                        else:
                            messagebox.showerror("Invalid Entries", "Title and Author entries only accept letters and digits\nYear entry must be between 1970 and " + currentYear
                                                 + "\nISBN number has to have 10 digits for books published BEFORE 2007 "
                                                   "and 13 digits for books published AFTER 2007")
    else:
        messagebox.showerror("Empty Entries", "Cannot execute due to some entries are empty")
    return False


#####################################################################
# Setting all commands for buttons
#####################################################################
def getSelectedRow(event):
    if len(backend.view()) != 0:  # avoid error when double-click the listbox while it's empty
        index = list_.curselection()[0]
        selected = list_.get(index)
        information = selected.split(", ")
        title.set(information[0])
        author.set(information[1])
        year.set(information[2])
        isbn.set(information[3])
        isbnEntry['state'] = 'disabled'
        oldTitle.set(title.get())
        oldAuthor.set(author.get())
        oldYear.set(year.get())

def clearCommand():
    title.set('')
    author.set('')
    year.set('')
    isbn.set('')
    isbnEntry['state'] = 'normal'

def viewCommand():
    list_.delete(0, END)  # delete all entry before re-click the button
    for row in backend.view():
        list_.insert(END, str(row).removeprefix('(').removesuffix(")").replace("'", ""))
    clearCommand()

def searchCommand():
    removeDuplicatedSpace()
    if len(title.get()) == 0 and len(author.get()) == 0 and len(year.get()) == 0 and len(isbn.get()) == 0:
        messagebox.showerror("Invalid Entries", "Please type in at least one entry")
    else:
        result = backend.search(title.get(), author.get(), year.get(), isbn.get())
        list_.delete(0, END)
        if len(result) == 0:
            list_.insert(END, "NO BOOKS FOUND! PLEASE TRY AGAIN WITH DIFFERENT INFORMATION")
        else:
            for row in result:
                list_.insert(END, str(row).removeprefix('(').removesuffix(")").replace("'", ""))

def addCommand():
    removeDuplicatedSpace()
    if validateEntries():
        if len(backend.isFound(isbn.get())) == 0:
            msg = messagebox.askokcancel("Add new book confirmation", "Title: " + title.get() + "\nAuthor: "
                                         + author.get() + "\nYear: " + year.get() + "\nISBN: " + isbn.get()
                                         + "\nAre you sure adding this book?")
            if msg:
                backend.insert(string.capwords(title.get()), string.capwords(author.get()), year.get(), isbn.get())
                viewCommand()  # after adding, clear all entries and renew listbox
                messagebox.showinfo("Insertion Status", "The data is added successfully")
        else:
            list_.delete(0, END)
            for row in backend.search("", "", "", isbn.get()):
                list_.insert(END, str(row).removeprefix('(').removesuffix(")").replace("'", ""))
            messagebox.showerror("Book Found", "A book with ISBN code " + isbn.get() + " is found in the database.\nPlease check the ISBN code again!")

def deleteCommand():
    if len(backend.isFound(isbn.get())) == 0:
        messagebox.showerror("Book not found", "No book found. Please check again the entries!")
    else:
        msg = messagebox.askokcancel("Delete Confirmation", "Title: " + title.get() + "\nAuthor: "
                                     + author.get() + "\nYear: " + year.get() + "\nISBN: " + isbn.get()
                                     + "\nAre you sure deleting this book?")
        if msg:
            backend.delete(title.get(), author.get(), year.get(), isbn.get())
            viewCommand()
            messagebox.showinfo("Deletion Status", "The data is deleted successfully")

def updateCommand():
    if validateEntries():
        if oldTitle.get() == title.get() and oldAuthor.get() == author.get() and oldYear.get() == year.get():
            messagebox.showinfo("Update Status", "No new info to be updated")
        else:
            msg = messagebox.askokcancel("Update Confirmation", "Title: " + title.get() + "\nAuthor: "
                                         + author.get() + "\nYear: " + year.get() + "\nISBN: " + isbn.get()
                                         + "\nPlease confirm new info")
            if msg:
                backend.update(string.capwords(title.get()), string.capwords(author.get()), year.get(), isbn.get())
                viewCommand()
                messagebox.showinfo("Update Status", "The data is updated successfully")

def closeCommand():
    msg = messagebox.askokcancel("Close program", "Close the program?")
    if msg:
        window.destroy()


#####################################################################
# Setting GUI
#####################################################################
window = Tk()
window.title("Book Inventory")
window.geometry("740x390")
window.resizable(False, False)

oldTitle = StringVar()
oldAuthor = StringVar()
oldYear = StringVar()


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
list_.bind('<Double-1>', getSelectedRow)  # double-click mode
scrollBar.config(command=list_.yview)  # create a scrollbar widget and set its command to the list box widget
slideBar.config(command=list_.xview)
slideBar.pack(side=BOTTOM, fill=X, expand=True, pady=10)
list_.pack(side=LEFT, fill=BOTH, expand=True, padx=15)
scrollBar.pack(side=RIGHT, fill=Y, expand=True)

viewButton = Button(window, text="View all", width=15, font=setFontSize(12), command=viewCommand)
searchButton = Button(window, text="Search entry", width=15, font=setFontSize(12), command=searchCommand)
addButton = Button(window, text="Add entry", width=15, font=setFontSize(12), command=addCommand)
updateButton = Button(window, text="Update selected", width=15, font=setFontSize(12), command=updateCommand)
deleteButton = Button(window, text="Delete selected", width=15, font=setFontSize(12), command=deleteCommand)
closeButton = Button(window, text="Close", width=15, font=setFontSize(12), command=closeCommand)
clearButton = Button(window, text="Clear entry", width=15, font=setFontSize(12), command=clearCommand)
viewButton.grid(row=2, column=3)
searchButton.grid(row=3, column=3)
addButton.grid(row=4, column=3)
clearButton.grid(row=5, column=3)
updateButton.grid(row=6, column=3)
deleteButton.grid(row=7, column=3)
closeButton.grid(row=8, column=3)

window.mainloop()
