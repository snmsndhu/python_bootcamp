# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx= 20, pady= 20)


canvas = Canvas(width=200, height=200)
pass_manager_img = PhotoImage(file = "logo.png")
canvas.create_image( 100, 100, image = pass_manager_img)
canvas.grid(column=2, row=1)

website_label = Label(text="Website:")
website_label.grid(column=1, row= 2)

website_input = Entry(width=35)
website_input.grid(row=2, column=2, columnspan=3)

email_label = Label(text= "Email/Username:")
email_label.grid(column=1, row=3)

email_input = Entry(width=35)
email_input.grid(row=3, column=2, columnspan=3)

password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

password_input = Entry(width=21)
password_input.grid(row=4, column=2)

generate_button = Button(text="Generate Password")
generate_button.grid(column=3, row=4)

add_button = Button(text="Add", width=36)
add_button.grid(column=2, row=5)
window.mainloop()