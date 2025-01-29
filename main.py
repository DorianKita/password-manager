from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_input.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_part = [random.choice(letters) for char in range(nr_letters)]
    symbol_part = [random.choice(symbols) for char in range(nr_symbols)]
    number_part = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = letter_part + symbol_part + number_part

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website)== 0 or len(email)== 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title= website, message=f"There are the details entered:\nEmail: {email}\n"
                                                               f"Password: {password}\nDo you want to save?")
        if is_ok:
            with open(file="data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")

            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas #
image = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100,100, image=image)
canvas.grid(row= 0, column= 1)

# Labels #

website_label = Label(text="Website:")
website_label.grid(row= 1, column= 0)

email_label = Label(text="Email/Username:")
email_label.grid(row= 2, column= 0)

password_label = Label(text="Password:")
password_label.grid(row= 3, column= 0)

# Inputs and buttons #

website_input = Entry(width= 35)
website_input.grid(row= 1, column= 1, columnspan= 2)
website_input.focus()

email_input = Entry(width= 35)
email_input.grid(row= 2, column = 1, columnspan = 2)
email_input.insert(0, "example@example.com")

password_input = Entry(width= 21)
password_input.grid(row= 3, column= 1)

generate_button = Button(text="Generate Password", width=10, command=generate_password)
generate_button.grid(row= 3, column= 2)

add_button = Button(text="Add", width=33, command=save_data)
add_button.grid(row= 4, column= 1, columnspan= 2)

window.mainloop()