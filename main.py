from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    with open(file="data.txt", mode="a") as file:
        file.write(f"{website} | {email} | {password}\n")

    website_input.delete(0, END)
    password_input.delete(0, END)

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

generate_button = Button(text="Generate Password", width=10)
generate_button.grid(row= 3, column= 2)

add_button = Button(text="Add", width=33, command=save_data)
add_button.grid(row= 4, column= 1, columnspan= 2)

window.mainloop()