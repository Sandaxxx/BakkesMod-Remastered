from tkinter import Tk
from tkinter import *
from tkinter import ttk, Label, Entry, Button, E, W, messagebox
from tkinter.filedialog import askopenfilename
import webbrowser


def openlink():
    get_url=webbrowser.open('https://www.twitch.tv')


root = Tk()
root.title("BakkesDaxInjectorCpp")
root.geometry("347x120")  # Largeur x Longueur
root.iconbitmap('BakkesDax.ico')
root.resizable(False, False)


photo = PhotoImage(file='Bakkes_font.png')
label = Label(root, image=photo)

label.pack()
root.mainloop()
 
