from tkinter import ttk
from tkinter import *
import tkinter as tk
from PIL import ImageDraw, ImageTk, Image
import ctypes

class About_Window(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("IT-cube Ростов")
        self.geometry(self.center_window(1300, 800))
        self.config(bg='#E6EEFF')
        self.iconbitmap('info.ico')
        self.protocol("WM_DELETE_WINDOW", self.dismiss)
        self.grab_set()

        # Создаем кнопку "Назад в меню"
        self.button_bg = self.create_rounded_rectangle(300, 80, 30, "#0074b4")  # Фон кнопки
        self.button_hover_bg = self.create_rounded_rectangle(300, 80, 30, "#3472d6")  # Цвет при наведении

        self.close_button = tk.Button(self, text="Назад в меню",
                                      image=self.button_bg,
                                      compound="center",
                                      fg="white",
                                      font=("Arial", 14, "bold"),
                                      bd=0,
                                      command=self.dismiss)
        self.close_button.place(x=990, y=10, width=300, height=80)
        self.close_button.image = self.button_bg
        self.close_button.bind("<Enter>", lambda e: self.on_enter(self.close_button))
        self.close_button.bind("<Leave>", lambda e: self.on_leave(self.close_button))
        self.info_bg = self.create_rounded_rectangle(350, 80, 30, "#0074b4")  # Фон заголовка

        self.info_label = tk.Label(self, image=self.info_bg,
                                   text="О нас", compound="center",
                                   fg="white",
                                   font=("Arial", 18, "bold"),
                                   bd=0)
        self.info_label.image = self.info_bg
        self.info_label.place(x=-50, y=0, width=350, height=80)
        self.title_bg = self.create_rounded_rectangle(400, 50, 20, "#0074b4")

        self.team_title = tk.Label(self, image=self.title_bg,
                                   text="Наша команда",
                                   compound="center",
                                   fg="white",
                                   font=("Arial", 20, "bold"),
                                   bd=0)
        self.team_title.image = self.title_bg
        self.team_title.place(x=450, y=220, width=400, height=50)

        # Фон для текста с эмодзи
        self.text_bg = self.create_rounded_rectangle(700, 300, 20, "#ffffff")

        # Основной текст с эмодзи
        self.info_text = tk.Label(self, image=self.text_bg,
                                  text=("Мы – команда IT-Куб Ростов, и на этом конкурсе мы представляем "
                                        "интерактивное приложение, созданное с использованием Python и Tkinter. 💻\n\n"
                                        "Наша программа объединяет простоту, креативность и современные технологии. 🎨 "
                                        "Мы доказали, что даже базовые инструменты Python могут быть мощным "
                                        "инструментом для реализации идей.\n\n"
                                        "Мы использовали функции, классы и циклы, чтобы создать удобный интерфейс, "
                                        "в котором каждый элемент проработан с вниманием к деталям. 🚀\n\n"
                                        "IT-Куб Ростов вдохновляет, творит и впечатляет. Готовы к технологиям будущего "
                                        "вместе с нами? ✨"),
                                  compound="center",
                                  fg="black",
                                  bg="#ffffff",
                                  wraplength=650,
                                  justify="center",
                                  font=("Arial", 16))
        self.info_text.image = self.text_bg
        self.info_text.place(x=300, y=300, width=700, height=300)

    def create_rounded_rectangle(self, width, height, radius, color):
        img = Image.new("RGBA", (width, height), (230, 238, 255, 256))
        draw = ImageDraw.Draw(img)
        draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=color)
        return ImageTk.PhotoImage(img)

    def center_window(self, width, height):
        """Центрирование окна относительно экрана."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        return f"{width}x{height}+{x}+{y}"

    def on_enter(self, button):
        button.config(image=self.button_hover_bg)

    def on_leave(self, button):
        button.config(image=self.button_bg)

    def dismiss(self):
        self.grab_release()
        self.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Скрываем главное окно
    about_window = About_Window()
    root.mainloop()
