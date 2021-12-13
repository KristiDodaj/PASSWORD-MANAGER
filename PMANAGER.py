from tkinter import *
import tkinter

########################
# GUI
########################

root = tkinter.Tk()
root.geometry('500x500')
root.title('PMANAGER')
root.resizable(False, False)
root.configure(background='#323232')

entry = tkinter.Entry(root)
entry.place(relx=0.5, rely=0.5, anchor=CENTER)


label = tkinter.Label(root, text='WELCOME TO PASSWORD MANAGER!', fg='white')
label.place(relx=0.5, rely=0.3, anchor=CENTER)
label.configure(background='#323232')

########################
# FUNCTIUONS
########################

def find_password(reference: str) -> None:
    """
    Finds the password for the given reference.
    """
    name = 'file directory'
    file = open(name, 'r')

    if len(reference) > 0 and reference != ' ' or '':

        new_list = []

        for line in file:
            if reference in line:
                new_list.append(line.split(':'))
        print(new_list[0][1])
        label.config(text=new_list[0][1])
        file.close()

def add_password(password: str) -> None:
    """
    Adds a new password to the file.
    """

    if len(password) > 0 and password != ' ' or '':
        name = 'file directory'
        file = open(name, 'a')

        file.write(password + '\n')
        file.close()

def remove_password(password: str) -> None:
    """
    Removes a password from the file.
    """

    if len(password) > 0 and len(password.strip()) != 0:
        name = 'file directory'
        file = open(name, 'r')
        lines = file.readlines()
        file.close()

        file = open(name, 'w')

        for line in lines:
            if password not in line:
                file.write(line + '\n')

        for line in lines:
            if password in line:
                lines.remove(line)
        file.close()


########################
# BUTTONS
########################

button = tkinter.Button(root, text='PASSWORD', command= lambda: find_password(entry.get()), bg = '#323232', highlightthickness = 0, bd = 0)
button.place(relx=0.5, rely=0.7, anchor=CENTER)

button2 = tkinter.Button(root, text='ADD', command= lambda: add_password(entry.get()), bg = '#323232', highlightthickness = 0, bd = 0)
button2.place(relx=0.5, rely=0.8, anchor=CENTER)

button3 = tkinter.Button(root, text='REMOVE', command= lambda: remove_password(entry.get()), bg = '#323232', highlightthickness = 0, bd = 0)
button3.place(relx=0.5, rely=0.9, anchor=CENTER)



root.mainloop()

