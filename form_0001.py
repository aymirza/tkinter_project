from tkinter import *
from tkinter import ttk,messagebox


window = Tk()
window.title("Tkinter form 0001")
window.geometry('750x350')
window.configure(background="gray")

def open_win():
    new=Toplevel(window)
    new.geometry("750x350")
    new.configure(background="gray")
    new.title("New Window")

def show_message():
    messagebox.showinfo("Gui Python",message.get())

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5,rely=.1, anchor="c")

btn1 = ttk.Button(text="Click Me", command=show_message)
btn1.place(x=30,y=30)
btn2 = ttk.Button(window,text="Open New Window", command=open_win)
btn2.place(x=30,y=65)


window.mainloop()