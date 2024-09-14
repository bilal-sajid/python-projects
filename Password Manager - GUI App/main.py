from tkinter import *
from tkinter import messagebox

from random import choice, randint, shuffle
import pyperclip


LOGO_PATH = "Password Manager - GUI App/logo.png"
DATA_PATH = "Password Manager - GUI App/data.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    # Remove old inputted password
    password_entry.delete(0,'end')

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password) # The password is already copied




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} \nPassword: {password} \nIs it okay to save?")

        if is_ok:
            # Create a .txt file which has all the Website, Email and Password information
            with open(DATA_PATH,'a') as file:
                content = website + " | " + email + " | " + password
                file.write(f"{content}\n")
            
                website_entry.delete(0,'end')
                password_entry.delete(0,'end')


# ---------------------------- UI SETUP ------------------------------- #

# Setting up Window
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)


# Setting up Logo
canvas = Canvas(width = 200, height = 200)
logo_img = PhotoImage(file = LOGO_PATH)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)


# For Website Section
website_label = Label(text = "Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)

website_entry.focus() # Focus the cursor at this entry

#For Email/Username Section
email_username_label = Label(text = "Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=39)
email_username_entry.grid(column=1, row=2, columnspan=2)

email_username_entry.insert(0, "example-email@gmail.com")

# For Password Section
password_label = Label(text = "Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)#, width=11)
generate_password_button.grid(column = 2, row = 3)

add_button = Button(text="Add", width=36, command= save_password)
add_button.grid(column = 1, row = 4, columnspan=2)






window.mainloop()