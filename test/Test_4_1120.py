from tkinter import *
import time


def what_day():

    day_init = {
        11:"1912年，中华民国正式成立。",
        14:"1969年，联合国大会第1904号决议通过了《联合国消除一切形式种族歧视宣言》。",
        501: "1886年，芝加哥劳工争取八小时工作制而被警察武装镇压。",
        523: "1943年，共产国际执行委员会主席团公开宣布《解散共产国际的决议》",
        1120: "1998年，Rita Hester被谋杀。",
        1123: "2021年，全斗焕死了。",
        1125: "1936年，日德签订反共产国际协定。",
        1129: "1947年，联大通过了第181号决议。",
        1212: "1979年，全斗焕发动了一场军事政变。",
        1214: "1960年，联大通过了第1514号决议。",
        1225: "1991年，苏联灭亡。",
    }

    day_time = int(time.strftime("%m%d", time.localtime()))

    try:

        print("━" * 65)
        print(day_init[day_time])
        print("━" * 65)

    except:

        pass

    day_time = int(time.strftime("%m%d", time.localtime()))

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


what_day()
