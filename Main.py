import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("Счётчик времени")
root.resizable(width=False, height=False)

hour = StringVar()
minute = StringVar()
second = StringVar()
cur_text = StringVar()

allow_to_press_button = True
counting = True

hour.set("0")
minute.set("0")
second.set("0")
cur_text.set("Введи время, котрое нужно засечь")

hourEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
hourEntry.place(x=80, y=60)
minuteEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=minute)
minuteEntry.place(x=130, y=60)
secondEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=second)
secondEntry.place(x=180, y=60)

lbl = Label(root, font=("Arial", 8, ""), textvariable=cur_text)
lbl.place(x=60, y=10)


def submit():
    global allow_to_press_button
    global counting
    if allow_to_press_button:
        counting = True
        cur_text.set("Отсчёт пошёл")
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
        while temp > -1:
            if counting == False:
                break
            allow_to_press_button = False
            mins, secs = divmod(temp, 60)
            hours = 0
            if mins > 60:
                hours, mins = divmod(mins, 60)

            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            root.update()
            time.sleep(1)

            if temp == 0:
                messagebox.showinfo("Счётчик времени", "Время вышло, отдохни")
                cur_text.set("Введи время, котрое нужно засечь")
            temp -= 1
        allow_to_press_button = True


def reset():
    global counting
    hour.set("0")
    minute.set("0")
    second.set("0")
    counting = False


btn = Button(root, text='Начать отсчёт', bd='5', bg="lime", command=submit, font=("Comic Sans MS", 9, "bold"))
btn.place(x=100, y=140)

btn2 = Button(root, text='Сброс', bd='5', bg="red", command=reset, font=("Comic Sans MS", 9, "bold"))
btn2.place(x=122, y=180)

root.mainloop()
