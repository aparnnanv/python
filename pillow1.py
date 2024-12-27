import tkinter as tk
from PIL import Image,ImageTk
root=tk.Tk()
image_path=("C://Users//USER//Pictures//about_files//img1.jpg")
image=Image.open(image_path)
background_image=ImageTk.PhotoImage(image)
canvas=tk.Canvas(root,width=image.width,height=image.height)
canvas.pack(fill="y",expand=True)
canvas.create_image(0,0,image=background_image)
