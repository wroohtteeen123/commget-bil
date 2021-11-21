import time

from tkinter import *


def what_day():

    day_time = int(time.strftime("%m%d", time.localtime()))

    if day_time == 501:

        print("━" * 65)
        print("今天是国际示威游行日。")
        print("━" * 65)

    if day_time == 1120:

        r_swt = Tk()

        r_swt.title("TDoR")

        Button(r_swt, text="跨性别死难者纪念日", bd=15).pack()

        Label(r_swt, text=" " * 60, bg="light blue").pack()
        Label(r_swt, text=" " * 60, bg="pink").pack()
        Label(r_swt, text=" " * 60, bg="white").pack()
        Label(r_swt, text=" " * 60, bg="pink").pack()
        Label(r_swt, text=" " * 60, bg="light blue").pack()

        Label(r_swt, text="").pack()

        Label(r_swt, text="悼念被谋杀的跨性别者🕯").pack()

        Label(r_swt, text=" " * 70).pack()

        r_swt.mainloop()

    if day_time == 1129:

        print("━" * 65)
        print("历史上的今天：。")
        print("1947年，联大通过了第181号决议。")
        print("━" * 65)

    if day_time == 1212:

        print("━" * 65)
        print("历史上的今天：。")
        print("1979年，全斗焕发动了一场军事政变。")
        print("━" * 65)

    if day_time == 1214:

        print("━" * 65)
        print("历史上的今天：。")
        print("1960年，联大通过了第1514号决议。")
        print("━" * 65)
