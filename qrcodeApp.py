import os
import tkinter as tk
from tkinter import END, NW

from PIL import Image, ImageTk
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
# create the main window
root = tk.Tk()


# set the window title
root.title("QR Code Generator App")

# create a label for the input box
label_input = tk.Label(root, text="Enter your input:", )
label_input.pack()

# create the input box
input_box = tk.Entry(root, width=50)
input_box.pack()

# create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10, padx=5)

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
label1 = tk.Label(image=None)


# define a function to be called when the button is clicked

def generateCode():
    links = input_box.get()
    print(links)
    qr.add_data(links)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    if not os.path.exists("images"):
        os.makedirs("images")
    img.save("images/qr_code.png")
    global qr_image
    qr_image = ImageTk.PhotoImage(file="images/qr_code.png")
    canvas.create_image(0, 0, anchor=NW, image=qr_image)


# create the generate qr code button
button1 = tk.Button(button_frame, text="create", bg="green", width=20, command=generateCode)
button1.pack(side=tk.LEFT)





root.mainloop()