#     ^__^
#    (oo)\_______
#    (__)\       )\/\
#         ||----w |
#         ||     ||
import numpy as np
import tkinter as tk
from PIL import Image, ImageDraw, ImageOps, ImageTk, ImageFont


class ImageDisplay:
    def __init__(self, image):
        self.image = Image.fromarray(np.array(image))
        self.img_left = ImageTk.PhotoImage(self.image)
        self.img_right = ImageTk.PhotoImage(ImageOps.mirror(self.image))
        self.update_left = True

    def update(self, label):
        if self.update_left:
            label.config(image=self.img_left)
            label.image = self.img_left
            self.update_left = False
        else:
            label.config(image=self.img_right)
            label.image = self.img_right
            self.update_left = True


text = """          
         ^__^
         (oo)\______
        (__)\_        _ )\/
             ||----w ||    
             ||         ||"""
width = 600
height = 600

image = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("comic.ttf", 40)
draw.text((30, 30), text, fill=(0, 0, 0), font=font)

image.save("example.png")

# Load the example.png image
img = Image.open("example.png")

# Get the height and width of the image
h, w, _ = np.array(img).shape

# Create the main window
root = tk.Tk()
root.title("Mad cow")

# Create a label to display the image
label = tk.Label(root)
label.pack()

img_display = ImageDisplay(img)


def update_image():
    img_display.update(label)
    root.after(500, update_image)


root.after(500, update_image)

# Start the main event loop
root.mainloop()
