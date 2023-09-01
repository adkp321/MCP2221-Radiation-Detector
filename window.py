from tkinter import *
from PIL import ImageTk, Image
import main
import pygame

root = Tk()
lab = Label(root, font=("Arial", 25))
lab.pack()

my_canvas = Canvas(root, width=700, height=700)
my_canvas.pack()

label_var = StringVar()

safe_img = ImageTk.PhotoImage(file="Basic_green_dot.png")
rad_img = ImageTk.PhotoImage(file="radiation_symbol.jpg")


def play():
    pygame.mixer.music.load("beep.mp3")
    pygame.mixer.music.play(loops=0)


def update():

    pygame.mixer.init()

    _, v_diode = main.get_voltage_g1()

    if v_diode < 3:
        rad_text = "Radiation Safe"
    if v_diode > 3:
        rad_text = "WARNING-Radiation"

    lab['text'] = rad_text

    # label_text = "Voltage value: {}".format(v_diode)  # Set the text of Label
    if v_diode < 3:
        print("Value: {} - Safe!".format(v_diode))
        my_canvas.create_image(350, 350, image=safe_img, anchor="center")
        # label_var.set(label_text)  # Updating the label

    elif v_diode > 3:
        print("Value: {} - Danger!".format(v_diode))
        # play() # Sound Effect
        my_canvas.create_image(350, 350, image=rad_img, anchor="center")
        # label_var.set(label_text)  # Updating the label

    root.after(100, update)  # Update command and rate, currently 10 updates per second or updating ever 0.1 second


update()


root.mainloop()
