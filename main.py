from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logoImg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoImg)
canvas.grid(row=0, column=1)

webLabel = Label(text="Website:")
webLabel.grid(row=1, column=0)
euNameLabel = Label(text="Email/Username:")
euNameLabel.grid(row=2, column=0)
passLabel = Label(text="Password:")
passLabel.grid(row=3, column=0)

webEntry = Entry(width=35)
webEntry.grid(row=1, column=1, columnspan=2)
euNameEntry = Entry(width=35)
euNameEntry.grid(row=2, column=1, columnspan=2)
passEntry = Entry(width=17)
passEntry.grid(row=3, column=1)

genPassButton = Button(text="Generate Password")
genPassButton.grid(row=3, column=2)
addButton = Button(text="Add", width=30)
addButton.grid(row=4, column=1, columnspan=2)


window.mainloop()