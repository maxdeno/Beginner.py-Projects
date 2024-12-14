from datetime import datetime
from time import sleep
from tkinter.ttk import *
from tkinter import *
from pygame import mixer

# window
window = Tk()
window.title("Alarm Clock")
window.geometry('400x150')





mixer.init()
alarm()

window.mainloop()