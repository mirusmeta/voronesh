import tkinter as tk
from tkinter import ttk
from PIL import ImageDraw, ImageTk, Image
import ctypes
from about import About_Window
from gallery import Gallery_Window

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def create_rounded_rectangle(width, height, radius, color):
    img = Image.new("RGBA", (width, height), (230, 238, 255, 256))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=color)
    return ImageTk.PhotoImage(img)


def on_enter(button):
    button.config(image=button_hover_bg)


def on_leave(button):
    button.config(image=button_bg)


def open_about_window():
    about_window = About_Window()


def open_gallery_window():
    gallery_window = Gallery_Window()

root = tk.Tk()
root.title("Информация о команде")

root.resizable(False, False)
root.iconbitmap('info.ico')
root.config(bg='#E6EEFF')

width = 1300
height = 800
x_offset = (root.winfo_screenwidth() - width) // 2
y_offset = (root.winfo_screenheight() - height) // 2
root.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

# Заголовок "Информация"
info_bg = create_rounded_rectangle(350, 80, 30, "#0074b4")  # Фон кнопки

info_label = tk.Label(root, image=info_bg, text="Информация", compound="center", fg="white", font=("Arial", 14, "bold"),
                      bd=0)
info_label.image = info_bg
info_label.place(x=-50, y=0, width=350, height=80)

# Загрузка изображения для фона квадрата
cube_image_path = 'images/fest_logo.PNG'  # Укажите путь к вашему изображению
cube_image = Image.open(cube_image_path)
cube_image_resized = cube_image.resize((400, 400))  # Изменяем размер изображения
cube_photo = ImageTk.PhotoImage(cube_image_resized)


# Основной квадрат с заголовком "IT-Куб Ростов"
frame_image_label = tk.Label(root, image=cube_photo, bg="#E6EEFF")  # Используем изображение как фон
frame_image_label.image = cube_photo
frame_image_label.place(x=150, y=150)

button_bg = create_rounded_rectangle(300, 80, 30, "#0074b4")  # Фон кнопки
button_hover_bg = create_rounded_rectangle(300, 80, 30, "#3472d6")  # Цвет при наведении

# Заголовок меню
text_menu = tk.Label(root, text="Меню", bg="#E6EEFF", fg="#5E5E5E", font=("Arial", 16, "bold"))
text_menu.place(x=984, y=190)

# "О нас" кнопка
button_about = tk.Button(root,
                        image=button_bg,
                        text="О нас",
                        compound="center",
                        command=open_about_window,
                        fg="white",
                        font=("Arial", 14, "bold"),
                        bd=0)
button_about.image = button_bg
button_about.place(x=880, y=250, width=300, height=80)
button_about.bind("<Enter>", lambda e: on_enter(button_about))
button_about.bind("<Leave>", lambda e: on_leave(button_about))

# "Галерея" кнопка
button_gallery = tk.Button(root,
                          image=button_bg,
                          text="Галерея",
                          compound="center",
                          command=open_gallery_window,
                          fg="white",
                          font=("Arial", 14, "bold"),
                          bd=0)
button_gallery.image = button_bg
button_gallery.place(x=880, y=360, width=300, height=80)
button_gallery.bind("<Enter>", lambda e: on_enter(button_gallery))
button_gallery.bind("<Leave>", lambda e: on_leave(button_gallery))

# "Участники" кнопка
button_participants = tk.Button(root,
                               image=button_bg,
                               text="Участники",
                               compound="center",
                               fg="white",
                               font=("Arial", 14, "bold"),
                               bd=0)
button_participants.image = button_bg
button_participants.place(x=880, y=470, width=300, height=80)
button_participants.bind("<Enter>", lambda e: on_enter(button_participants))
button_participants.bind("<Leave>", lambda e: on_leave(button_participants))

root.mainloop()