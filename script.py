from tkinter import *
import tkinter.font as font

window = Tk()
window.title("Book Inventory")
window.geometry("580x300")
window.resizable(False, False)

fontSize = font.Font(size=12)

titleL = Label(window, text="Title", height=2, width=10, font=fontSize)
titleL.grid(row=0, column=0)
title = StringVar()
titleEntry = Entry(window, width=20, textvariable=title, font=fontSize)
titleEntry.grid(row=0, column=1)

authorL = Label(window, text="Author", height=2, width=10, font=fontSize)
authorL.grid(row=0, column=2)
author = StringVar()
authorEntry = Entry(window, width=20, textvariable=author, font=fontSize)
authorEntry.grid(row=0, column=3)

yearL = Label(window, text="Year", height=2, width=10, font=fontSize)
yearL.grid(row=1, column=0)
year = StringVar()
yearEntry = Entry(window, width=20, textvariable=year, font=fontSize)
yearEntry.grid(row=1, column=1)

isbnL = Label(window, text="ISBN", height=2, width=10, font=fontSize)
isbnL.grid(row=1, column=2)
isbn = StringVar()
isbnEntry = Entry(window, width=20, textvariable=isbn, font=fontSize)
isbnEntry.grid(row=1, column=3)

# create Frame() object to hold only the listbox and scrollbar
frame = Frame(window)
frame.grid(row=2, column=0, rowspan=6, columnspan=3)

scrollBar = Scrollbar(frame)
scrollBar.pack(side=RIGHT, fill=Y)
list_ = Listbox(frame, yscrollcommand=scrollBar.set, width=40, font=fontSize)  # communicate back to the scrollbar
for line in range(100):
    list_.insert(END, "This is line number " + str(line))
list_.pack(side=LEFT, fill=BOTH)
scrollBar.config(command=list_.yview)  # create a scrollbar widget and set its command to the list box widget

viewButton = Button(window, text="View all", width=12, font=fontSize)
searchButton = Button(window, text="Search entry", width=12, font=fontSize)
addButton = Button(window, text="Add entry", width=12, font=fontSize)
updateButton = Button(window, text="Update", width=12, font=fontSize)
deleteButton = Button(window, text="Delete", width=12, font=fontSize)
closeButton = Button(window, text="Close", width=12, font=fontSize)
viewButton.grid(row=2, column=3)
searchButton.grid(row=3, column=3)
addButton.grid(row=4, column=3)
updateButton.grid(row=5, column=3)
deleteButton.grid(row=6, column=3)
closeButton.grid(row=7, column=3)


window.mainloop()
