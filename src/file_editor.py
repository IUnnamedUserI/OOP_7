#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, состоящую из однострочного и многострочного текстовых
полей и двух кнопок "Открыть" и "Сохранить". При клике на первую должен
открываться на чтение файл, чье имя указано в поле класса Entry, а содержимое
файла должно загружаться в поле типа Text. При клике на вторую кнопку текст
введенный пользователем в экземпляр Text, должен сохраняться в файле под
именем, которое пользователь указал в однострочном текстовом поле. Файлы будут
читаться и записываться в том же каталоге, что и файл скрипта, если указывать
имена файлов без адреса. Для выполнения практической работы вам понадобится
функция open языка Python и методы файловых объектов чтения и записи.
"""

from tkinter import Tk, Frame, Entry, Button, Text, END, LEFT
from tkinter import messagebox


def open_file():
    """
    Открывает файл и загружает его содержимое в текстовое поле.
    """
    try:
        filename = entry.get()
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            text_field.delete(1.0, END)
            text_field.insert(1.0, content)
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл не найден!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


def save_file():
    """
    Сохраняет содержимое текстового поля в файл.
    """
    try:
        filename = entry.get()
        content = text_field.get(1.0, END)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        messagebox.showinfo("Успех", "Файл успешно сохранен!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


def main():
    """Основная функция для создания графического интерфейса."""
    global entry, text_field

    root = Tk()
    root.title("Редактор файлов")
    root.geometry("600x400")

    input_frame = Frame(root)
    input_frame.pack(pady=10)

    entry = Entry(input_frame, width=40)
    entry.pack(side=LEFT, padx=5)

    open_button = Button(input_frame, text="Открыть", width=10,
                         command=open_file)
    open_button.pack(side=LEFT, padx=5)

    save_button = Button(input_frame, text="Сохранить", width=10,
                         command=save_file)
    save_button.pack(side=LEFT, padx=5)

    text_field = Text(root, width=60, height=20)
    text_field.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
