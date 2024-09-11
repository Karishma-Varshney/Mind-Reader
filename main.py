from tkinter import *
from tkinter import messagebox


def read():
    messagebox.showinfo(title='Mind Reader', message=f"You're thinking of the number {entry.get()}.")


window = Tk()
window.title("Mind Reader")
window.config(padx=10, pady=10)

label = Label(text="Think of a number between 1 and 10:")
label.pack(padx=20, pady=20)

entry = Entry(width=10)
entry.pack(padx=20, pady=20)

button = Button(text='Read my mind', command=read)
button.pack(padx=20, pady=20)


window.mainloop()
