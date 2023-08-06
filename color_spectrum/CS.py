from tkinter import *
from PIL import Image, ImageTk

open = r"images/rainbow.jpg"
image = Image.open(open) #to set the tkineter window's height ann width
window = Tk()
window.geometry(f"{image.width}x{image.height}")


def RGB(pos):
    x= pos.x
    y= pos.y
    rgb =image.getpixel((x, y))
    print(f"Color at ({x}, {y}): RGB({rgb[0]}, {rgb[1]}, {rgb[2]})") #0=red, 1=green, 2=blue


canvas = Canvas(window, width=image.width, height=image.height) #canva needs to be packed hust like other widgets(place works as well)
canvas.pack()

photo = ImageTk.PhotoImage(image) # compatible format
canvas.create_image(0,0, anchor=NW,image=photo) #ancher NW means the pic is anchored to the north west
canvas.bind("<Button-1>",RGB)# left click activates color function

window.mainloop()
