from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def rando_pw():
    pw_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pw_letters = [random.choice(letters) for _ in range(nr_letters)]
    pw_nums = [random.choice(numbers) for _ in range(nr_numbers)]
    pw_sym = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = pw_sym + pw_nums + pw_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    pw_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def hit_add():
    web = web_input.get()
    user = email_input.get()
    pw = pw_input.get()
    length = min(len(web), len(user), len(pw))
    my_data = {
        web: {
            "email": user,
            "password": pw,
        }
    }
    if length == 0:
        messagebox.showerror("Error", "Valid input required for all fields")
    else:
        try:
            with open("myFile.json", "r") as file:
                # reading old data and checking if it's empty
                file_content = file.read()
                if file_content:
                    old_data = json.loads(file_content)
                else:
                    old_data = {}

        except FileNotFoundError:
            old_data = {}

        old_data.update(my_data)

        with open("myFile.json", "w") as file:
            json.dump(old_data, file, indent=5)

        web_input.delete(0, END)
        pw_input.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def searching():
    web = web_input.get()
    if not web:
        messagebox.showerror("Error", "Please enter  a website to search")
        return

    try:
        with open("myFile.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "Data file not found.")
        return
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Data file is corrupt or empty.")
        return

    if web in data:
        user_info = data[web]
        message = f"Website: {web}\nEmail/Username: {user_info['email']}\nPassword: {user_info['password']}"
        messagebox.showinfo("Found Credentials", message)
    else:
        messagebox.showinfo("Not Found", f"No details found for the website: {web}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("G-Lock")
window.config(pady=50, padx=50)

# canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)

# input fields
web_input = Entry()
web_input.grid(row=1, column=1, sticky="EW")
web_input.focus()

email_input = Entry()
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(0, "1234@gmail.com")

pw_input = Entry()
pw_input.grid(row=3, column=1, sticky="EW")

# button

add_button = Button(text="Add", command=hit_add)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

gen_button = Button(text="Generate Password", command=rando_pw)
gen_button.grid(row=3, column=2, sticky="EW")

search_button = Button(text="Search", command=searching )
search_button.grid(row=1, column=2, sticky="EW")

window.mainloop()
