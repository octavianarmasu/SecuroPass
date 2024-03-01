import tkinter as tk
import tkinter.font as tkFont
import crack_time as ck


def isDigit(letter):
    if letter >= '0' and letter <= '9':
        return True
    return False


def isSpecial(letter):
    if isDigit(letter) == False and not (letter.islower()) and not (letter.isupper()):
        return True
    return False


def passCheck(password):
    required = {'upper': False, 'lower': False,
                'digit': False, 'special': False, 'length': False}
    # checking how strong is the password
    if len(password) >= 8:
        required['length'] = True
    for letter in password:
        if letter.islower():
            required['lower'] = True
        if letter.isupper():
            required['upper'] = True
        if isDigit(letter):
            required['digit'] = True
        if isSpecial(letter):
            required['special'] = True
    return required


def passStrength(n):
    # printing the strength of the password
    if n == 1:
        return "Very weak password!"
    elif n == 2:
        return "Weak password!"
    elif n == 3:
        return "Decent password!"
    elif n == 4:
        return "Strong password!"
    elif n == 5:
        return "Very strong password!"


def checkPasswords():
    if password.get() == password2.get():
        error_message.config(text="", fg="white")
        requirementsMet = sum(
            value for value in passCheck(password.get()).values())
        password_strength = passStrength(requirementsMet)
        crack_message = ck.print_time(password.get())
        strength_message.config(text=password_strength, fg="blue")
        crack.config(text=crack_message, fg="green")

    else:
        strength_message.config(text="", fg="white")
        crack.config(text="", fg="white")
        error_message.config(text="Passwords do not match!", fg="red")
        password.delete(0, tk.END)
        password2.delete(0, tk.END)


app = tk.Tk()
app.title("Password Checker App")
app.geometry("400x200")
app.config(bg="white")

welcome_label = tk.Label(
    app, text="Welcome to the Password Checker App", bg="white")
welcome_label.pack(pady=(10, 5))

instruction_label = tk.Label(app, text="Your password should contain a lower case letter,"
                                       " an upper case letter, a digit, a special character.\n"
                                       "It should be at least 8 characters long.", bg="white", justify=tk.LEFT)
instruction_label.pack(pady=(5, 10))
password_label = tk.Label(app, text="Enter Password:", bg="white")
password_label.pack()

password = tk.Entry(app, show="*")
password.pack()

reenter_password_label = tk.Label(app, text="Re-enter Password:", bg="white")
reenter_password_label.pack()

password2 = tk.Entry(app, show="*")
password2.pack()

feedback_font = tkFont.Font(size=14, weight="bold")

error_message = tk.Label(app, text="", bg="white", font=feedback_font)
error_message.pack(pady=(5, 0))

strength_message = tk.Label(app, text="", bg="white", font=feedback_font)
strength_message.pack(pady=(5, 0))

crack_font = tkFont.Font(size=12)
crack = tk.Label(app, text="", bg="white", font=crack_font)
crack.pack(pady=(5, 1))

check_button = tk.Button(app, text="Check Password", command=checkPasswords)
check_button.pack(pady=(10, 0))

app.mainloop()
