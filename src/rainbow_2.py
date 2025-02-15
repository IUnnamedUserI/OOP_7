#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Перепишите программу из пункта 8 так, чтобы кнопки были в ряд.
"""

from tkinter import Tk, Label, Entry, Button, Frame, END, LEFT


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
    root.geometry("300x100")

    color_label = Label(root, text="Выберите цвет", font=("Arial", 12))
    color_label.pack(pady=5)

    text_field = Entry(root, width=20)
    text_field.pack(pady=5)

    colors = [
        ("Красный", "#ff0000"),
        ("Оранжевый", "#ff7f00"),
        ("Желтый", "#ffff00"),
        ("Зеленый", "#00ff00"),
        ("Голубой", "#007dff"),
        ("Синий", "#0000ff"),
        ("Фиолетовый", "#7400ff")
    ]

    button_frame = Frame(root)
    button_frame.pack()

    for color_name, color_code in colors:
        button = Button(
            button_frame,
            text="",
            bg=color_code,
            fg="black",
            width=3,
            command=lambda name=color_name, code=color_code:
                set_color(name, code)
        )
        button.pack(side=LEFT, padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
