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
def saveDataToJson():
    messagebox.showinfo("Gui Python", data)


message = StringVar()

data = {"languages":"Python","languages":"Java","languages":"CSharp"}

message_entry = Entry(textvariable=message)
message_entry.place(x=250,y=40, anchor="c")

entry1 = Entry(textvariable=message)
entry1.place(x=250,y=75, anchor="c")

entry1 = Entry(textvariable=message)
entry1.place(x=250,y=110, anchor="c")

btn1 = ttk.Button(text="Click Me", command=show_message)
btn1.place(x=20,y=35)
btn2 = ttk.Button(window,text="Open New Window", command=open_win)
btn2.place(x=20,y=65)
btn2 = ttk.Button(window,text="Save to Json", command=open_win)
btn2.place(x=20,y=95)


window.mainloop()