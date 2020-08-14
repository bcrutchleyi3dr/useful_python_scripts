from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image    

def showImage():
        lbl1.configure(image=image_tk)
        btn.configure(text = "Turn Hazards On", command=showImage1)

def showImage1(): 
        lbl1.configure(image=image_tk1)
        btn.configure(text = "Turn Hazards Off", command=showImage)     

root = Tk()    
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

fname = "a.jpg"
image_tk = ImageTk.PhotoImage(Image.open("left.png"))

fname1 = "b.jpg"
image_tk1 = ImageTk.PhotoImage(Image.open("left_marked.png"))  # new image object


btn = ttk.Button(c, text="load image", command=showImage)
lbl1 = ttk.Label(c)
btn.grid(column=0, row=0, sticky=N, pady=5, padx=5)
lbl1.grid(column=1, row=1, sticky=N, pady=5, padx=5)

root.mainloop()
