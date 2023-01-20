from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for a in range(nr_letters)]
    password_list += [random.choice(numbers) for a in range(nr_numbers)]
    password_list += [random.choice(symbols) for a in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, 'end')
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    if website_input.get() == "" or password_input.get() == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_it = messagebox.askokcancel(title=website_input.get(), message=f"There are your details entered:"
                                                                          f"\nEmail : {email_input.get()}"
                                                                          f"\nPassword : {password_input.get()}"
                                                                          f"\nis it ok to save?")

        if is_it:
            with open("data.txt", "a") as data:
                data.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()} \n")
            website_input.delete(0, 'end')
            password_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=43)
website_input.grid(row=1, column=1, columnspan=2, sticky=W)
website_input.focus()

email_input = Entry(width=43)
email_input.insert(0, "mohammed1212345@gmail.com")
email_input.grid(row=2, column=1, columnspan=2, sticky=W)

password_input = Entry(width=24)
password_input.grid(row=3, column=1, sticky=W)

generate_password_button = Button(text="Generate Password", command=password_gen)
generate_password_button.grid(row=3, column=1, columnspan=2, sticky=E)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)

window.mainloop()
