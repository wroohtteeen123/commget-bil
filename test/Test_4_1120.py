from tkinter import *
import time


def what_day():

    day_time = int(time.strftime("%m%d", time.localtime()))

    if day_time == 1120:

        show_window_transgender()


def show_window_transgender():

    root = Tk()

    root.title("TDoR")

    Button(root, text="跨性别死难者纪念日", bd=15).pack()

    Label(root, text=" " * 60, bg="light blue").pack()
    Label(root, text=" " * 60, bg="pink").pack()
    Label(root, text=" " * 60, bg="white").pack()
    Label(root, text=" " * 60, bg="pink").pack()
    Label(root, text=" " * 60, bg="light blue").pack()

    Label(root, text="").pack()

    Label(root, text="悼念被谋杀的跨性别者🕯").pack()

    Label(root, text=" " * 70).pack()

    root.mainloop()


what_day()
show_window_transgender()
