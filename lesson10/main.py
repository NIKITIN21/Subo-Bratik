from tkinter import *

root = Tk()
width = 700
height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_offset = (screen_width - width) //2
y_offset = (screen_height - height) //2
root.geometry(f"{width}x{height}+{x_offset}+{y_offset}")
root.title("Викторина")
root.resizable(False, False)
QUEST = Label(text="", font=("Arial", 16))
QUEST.place(anchor="center", relx=0.5, rely=0.15)

info = Label(text="", font=("Arial", 12), fg="red")
info.place(anchor="center", relx=0.5, rely=0.25)
buttons = []

for i in range(1, 5):
    btn = Button(width=50, height=1, font=("Arial", 14))
    btn.place(anchor="center", relx=0.5, rely=0.25+0.15*i)
    buttons.append(btn)

root.mainloop()