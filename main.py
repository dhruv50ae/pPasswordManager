from tkinter import *
from tkinter import messagebox
import random
import pyperclip

def genPass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    passEntry.insert(0, password)


def save():
    websiteCreds = webEntry.get()
    euNameCreds = euNameEntry.get()
    passCreds = passEntry.get()

    if len(websiteCreds) == 0 or len(euNameCreds) == 0 or len(passCreds) == 0:
        messagebox.showinfo(title="⚠ Data Input Error ⚠",
                            message="Please make sure you haven't left any fields empty. ")
    else:

        isOk = messagebox.askokcancel(title=websiteCreds,
                                      message=f"These are the details you entered: \nEmail/Username: {euNameCreds} \nPassword: {passCreds} \nIs it okay to save?")
        if isOk:
            with open("data.txt", "a") as data:
                data.write(f"{websiteCreds} | {euNameCreds} | {passCreds}\n")
            webEntry.delete(0, END)
            passEntry.delete(0, END)


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
webEntry.focus()
euNameEntry = Entry(width=35)
euNameEntry.grid(row=2, column=1, columnspan=2)
euNameEntry.insert(0, "Fryost50AE")
passEntry = Entry(width=17)
passEntry.grid(row=3, column=1)

genPassButton = Button(text="Generate Password", command=genPass)
genPassButton.grid(row=3, column=2)
addButton = Button(text="Add", width=30, command=save)
addButton.grid(row=4, column=1, columnspan=2)

window.mainloop()
