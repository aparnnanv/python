from tkinter import *
root=Tk()
f1=Frame(root,padx=200,pady=200,bg="yellow")
f1.pack()

def new1():
    next1=Tk()
    c=Canvas(next1,height=300,width=200,bg="green")
    c.place(x=20,y=70)
    square=c.create_line(2,2,4,4)

b1=Button(f1,text="square",bg="pink",command=new1)
b1.pack()

root.mainloop()
