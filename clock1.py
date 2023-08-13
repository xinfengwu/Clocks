from tkinter import *
from time import strftime

def update():
  time_string = strftime("%I:%M:%S %P")
  time_label.config(text=time_string)

  day_string = strftime("%A")
  day_label.config(text=day_string)

  date_string = strftime("%B %d,%Y")
  date_label.config(text=date_string)

  window.after(1000,update)

window = Tk()
window.title("Clock1")

time_label = Label(window,font=("Ubuntu Mono",100,"bold"),fg="#00FF00",bg="black")
time_label.pack(anchor='center')

day_label = Label(window,font=("FreeMono",25,"bold"))
day_label.pack(anchor='center')

date_label = Label(window,font=("FreeMono",25,"bold"))
date_label.pack(anchor='center')


update()
window.mainloop()

