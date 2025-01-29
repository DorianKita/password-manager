from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

image = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200)
canvas.create_image(100,100, image=image)
canvas.grid(row= 0, column= 1)

website_label = Label(text="Website:")
website_label.grid(row= 1, column= 0)

email_label = Label(text="Email/Username:")
email_label.grid(row= 2, column= 0)

password_label = Label(text="Password:")
password_label.grid(row= 3, column= 0)

window.mainloop()