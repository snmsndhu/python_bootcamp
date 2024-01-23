from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_input.get()
    email = email_input.get()
    website_password = password_input.get()
    if len(website_name) == 0 or len(website_password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title= website_name, message=f"These are the details entered: \nEmail: {email} \nPassword: {website_password} \n Is it ok to save ?")
        if is_ok:
            with open("data.txt", mode= "a") as data_file:
                data_file.write(f"{website_name} | {email} | {website_password} \n")
                website_input.delete(0, END)
                password_input.delete(0, END)


    
# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx= 80, pady= 80)


canvas = Canvas(width=200, height=200)
pass_manager_img = PhotoImage(file = "logo.png")
canvas.create_image( 100, 100, image = pass_manager_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row= 1)

email_label = Label(text= "Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "address@email.com")
password_input = Entry(width=18)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command= save)
add_button.grid(column=1,columnspan=2, row=4)
window.mainloop()