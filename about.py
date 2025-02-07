from tkinter import ttk
from tkinter import *
import tkinter as tk

from PIL import ImageDraw, ImageTk, Image

class About_Window(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("IT-cube Ростов")
        self.geometry('1300x800')
        self.config(bg='#E6EEFF')
        self.protocol("WM_DELETE_WINDOW", self.dismiss)  # перехватываем нажатие на крестик
        self.grab_set()

        self.button_bg = self.create_rounded_rectangle(300, 80, 30, "#0074b4")  # Фон кнопки
        self.button_hover_bg = self.create_rounded_rectangle(300, 80, 30, "#3472d6")

        self.close_button = tk.Button(self, text="Назад в меню",
                                      image=self.button_bg,
                                      compound="center",
                                      fg="white",
                                      font=("Arial", 14, "bold"),
                                      bd=0,
                                      command=self.dismiss)
        self.close_button.place(x=1000, y=30, width=300, height=80)
        # Цвет при наведении
        self.close_button.image = self.button_bg
        self.button_hover_bg = self.create_rounded_rectangle(300, 80, 30, "#3472d6")  # Цвет при наведении
        self.button_bg = self.create_rounded_rectangle(300, 80, 30, "#0074b4")
        self.close_button.bind("<Enter>", lambda e: self.on_enter(self.close_button))
        self.close_button.bind("<Leave>", lambda e: self.on_leave(self.close_button))

    def create_rounded_rectangle(self, width, height, radius, color):
        img = Image.new("RGBA", (width, height), (230, 238, 255, 256))
        draw = ImageDraw.Draw(img)
        draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=color)
        return ImageTk.PhotoImage(img)

    def on_enter(self, button):
        button.config(image=self.button_hover_bg)

    def on_leave(self, button):
        button.config(image=self.button_bg)

    def dismiss(self):
        self.grab_release()
        self.destroy()







