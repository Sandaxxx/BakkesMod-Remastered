# Developped by Sandax#3984

from tkinter import Tk
from tkinter import *
from tkinter import ttk, Label, Entry, Button, E, W, messagebox
from tkinter.filedialog import askopenfilename
import webbrowser # for open link to your browser 

# REDIRECT LINK IN LINKS
def linkbakkes():
    get_url=webbrowser.open('https://bakkesmod.com')

def linktwitch():
    get_url=webbrowser.open('https://www.twitch.tv/sandax')

def linkdiscord():
    get_url=webbrowser.open('https://www.twitter.com/sandax_')

def linktwitter():
    get_url=webbrowser.open('https://www.twitch.tv')

def linkgithub():
    get_url=webbrowser.open('https://www.github.com/Sandaxxx/BakkesMod-Remastered')


# ROOT TK
root = Tk()
root.title("BakkesDaxInjectorCpp")
root.geometry("347x120")  # Largeur x Longueur
root.iconbitmap('BakkesDax.ico')
root.resizable(False, False)

# IMAGE 
photo = PhotoImage(file='Bakkes_font.png')
label = Label(root, image=photo)

# MENU FILES 
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open BakkesDax folder ")
filemenu.add_command(label="Check for updates")
filemenu.add_command(label="Reinstall")
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# MENU LINKS 
linkmenu = Menu(menubar, tearoff=0)
linkmenu.add_command(label="★ BakkesDax.com", background='#e9d8a6', command=linkbakkes)
linkmenu.add_command(label="★ BakkesDax Twitch", background='#9b5de5', command=linktwitch)
linkmenu.add_command(label="★ BakkesDax Discord", background='#7289da', command=linkdiscord)
linkmenu.add_command(label="★ BakkesDax Twitter", background='#00b4d8', command=linktwitter)
linkmenu.add_command(label="★ BakkesDax Github", background='#00b4d8', command=linkgithub)
menubar.add_cascade(label="Links", menu=linkmenu)

# MENU SETTINGS
Settingsmenu = Menu(menubar, tearoff=0)
Settingsmenu.add_command(label="Enable safe mode")
Settingsmenu.add_command(label="Run on startup")
Settingsmenu.add_command(label="Hide when minimized")
Settingsmenu.add_command(label="Minimized on start")
Settingsmenu.add_command(label="Manually select BakkesDax folder")
Settingsmenu.add_command(label="Set injection timeout(2500)")
Settingsmenu.add_command(label="Disable warnings")
Settingsmenu.add_command(label="Opti-in to beta releases")
menubar.add_cascade(label="Settings", menu=Settingsmenu)

# MENU HELP
Helpmenu = Menu(menubar, tearoff=0)
Helpmenu.add_command(label="Check injection")
Helpmenu.add_command(label="Troubleshooting")
Helpmenu.add_command(label="Show version info")
menubar.add_cascade(label="Help", menu=Helpmenu)

#TEXT < IMAGE (simple)
# label = Label(root, text="Rocket League (Epic Games): up to date.\nㅤ ㅤㅤㅤUninjected, waiting for user to start Rocket League", width=100, height=100)

# RUN 
root.config(menu=menubar)
label.pack()
root.mainloop()