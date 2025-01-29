from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

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

email_input = Entry(width= 35)
email_input.grid(row= 2, column = 1, columnspan = 2)

password_input = Entry(width= 20)
password_input.grid(row= 3, column= 1)

generate_button = Button(text="Generate Password", width=11)
generate_button.grid(row= 3, column= 2)

add_button = Button(text="Add", width=33)
add_button.grid(row= 4, column= 1, columnspan= 2)

window.mainloop()