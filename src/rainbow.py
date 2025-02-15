#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, состоящую из семи кнопок, цвета которых соответствуют
цветам радуги. При нажатии на ту или иную кнопку в текстовое поле должен
вставляться код цвета, а в метку – название цвета. Коды цветов в
шестнадцатеричной кодировке: #ff0000 – красный, #ff7d00 – оранжевый,
#ffff00 – желтый, #00ff00 – зеленый, #007dff – голубой, #0000ff – синий,
# #7d00ff – фиолетовый.
"""

from tkinter import Tk, Label, Entry, Button, END


def set_color(color_name, color_code):
    """
    Устанавливает код цвета в текстовое поле и название цвета в метку.
    """
    text_field.delete(0, END)
    text_field.insert(0, color_code)
    color_label.config(text=color_name)


def main():
    """Основная функция для создания графического интерфейса."""
    global text_field, color_label

    root = Tk()
    root.title("Цвета радуги")
    root.geometry("150x300")

    color_label = Label(root, text="Выберите цвет", font=("Arial", 14))
    color_label.pack(pady=10)

    text_field = Entry(root, width=15)
    text_field.pack(pady=10)

    colors = [
        ("Красный", "#ff0000"),
        ("Оранжевый", "#ff7f00"),
        ("Желтый", "#ffff00"),
        ("Зеленый", "#00ff00"),
        ("Голубой", "#007dff"),
        ("Синий", "#0000ff"),
        ("Фиолетовый", "#7400ff")
    ]

    for color_name, color_code in colors:
        button = Button(
            root,
            text="",
            bg=color_code,
            fg="black",
            width=15,
            command=lambda name=color_name, code=color_code:
                set_color(name, code)
        )
        button.pack(pady=2)

    root.mainloop()


if __name__ == "__main__":
    main()
