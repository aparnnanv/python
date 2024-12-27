from tkinter import *
window=Tk()
window.title("new window")

def login():
    lg=Tk()
    lg.config(bg="brown")
def menu():
    mu=Tk()
    l1=Label(mu,text="food items")
    

    listbox=Listbox(mu,height=10,width=10,bg="black",fg="white")
    label=Label(mu,text="food items")
    l1.place(x=300,y=400)
    listbox.insert(1,"pizza")
    listbox.insert(2,"biriyani")
    listbox.insert(3,"icecream")
    listbox.insert(4,"vada")
    label.pack()
    listbox.pack()
b2=Button(window,text="menu",padx=10,pady=10,command=menu)
b2.place(x=300,y=80)

b1=Button(window,text="login",padx=10,pady=10,command=login)
b1.place(x=400,y=80)
window.mainloop()
