from datetime import datetime
from time import sleep

from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image
from pygame import mixer


from thread import Thread

# window
window = Tk()
window.title("Alarm Clock")
window.geometry('400x150')
window.configure(bg="white")

# frame
frame_line = Frame(window, width= 400, height=5, bg="Blue")
frame_line.grid(row=0,column=0)

# frame body
frame_body = Frame(window, width= 400, height=290, bg="Black")
frame_body.grid(row=1,column=0)

# configure frame body
img = Image.open("Icon.png")
img.resize((1500,1300))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, height= 100, image= img, bg= "Black")
app_image.place(x=10,y=10)


# layout
name = Label(frame_body, text= "Time", height= 1, font="Ivy 15 bold", fg="Blue", bg= "Black")
name.place(x=85, y= 10)

# hour
hour = Label(frame_body, text= "Hour", height= 1, font="Ivy 13 bold", fg="Blue", bg= "Black")
hour.place(x=85, y= 40)
c_hour = Combobox(frame_body, width= 2, font="arial 15")
c_hour["values"] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09",
    "10", "11", "12")
c_hour.current(0)
c_hour.place(x=88, y=63)

# minute
min= Label(frame_body, text= "Min", height= 1, font="Ivy 13 bold", fg="Blue", bg= "Black")
min.place(x=140, y= 40)
c_min = Combobox(frame_body, width= 2, font="arial 15")
c_min["values"] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09",
    "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
    "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
    "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
    "40", "41", "42", "43", "44", "45", "46", "47", "48", "49",
    "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_min.current(0)
c_min.place(x=138, y=63)

# seconds
sec= Label(frame_body, text= "Sec", height= 1, font="Ivy 13 bold", fg="Blue", bg= "Black")
sec.place(x=190, y= 40)
c_sec = Combobox(frame_body, width= 2, font="arial 15")
c_sec["values"] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09",
    "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
    "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
    "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
    "40", "41", "42", "43", "44", "45", "46", "47", "48", "49",
    "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_sec.current(0)
c_sec.place(x=188, y=63)

# period
period= Label(frame_body, text= "Period", height= 1, font="Ivy 13 bold", fg="Blue", bg= "Black")
period.place(x=237, y= 40)
c_period= Combobox(frame_body, width= 3, font="arial 15")
c_period["values"] = ("AM", "PM")
c_period.current(0)
c_period.place(x=238, y=63)

# Activate alarm
def activate_alarm():
    t = Thread(target=alarm)
    t.start()

# deactivate alarm
def deactivate_alarm():
    print("Hope you are awake!", selected.get())
    mixer.music.stop()


selected = IntVar()

# Activate button
rad1 = Radiobutton(frame_body, font= "Arial 10 bold", value=1, text="Activate",bg="Black", fg="Dark green",
                   command=activate_alarm, variable=selected)
rad1.place(x=85, y=95)



# load and play music
def sound_alarm():
    mixer.music.load("alarm1.mp3")
    mixer.music.play()
    selected.set(0)

    rad2 = Radiobutton(frame_body, font="Arial 10 bold", value=2, text="Deactivate", bg="Black", fg="Dark green",
                       command=deactivate_alarm, variable=selected)
    rad2.place(x=185, y=95)

# setting the date and time
def alarm():
    while True:
        control = selected.get()
        print(control)

        alarm_hour = c_hour.get()
        alarm_min = c_min.get()
        alarm_sec = c_sec.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()

        now = datetime.now()

        hour = now.strftime("%H")
        min = now.strftime("%M")
        sec = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_min == min:
                        if alarm_sec == sec:
                            print("Time to raise and shine!")
                            sound_alarm()

        sleep(1)

mixer.init()
window.mainloop()