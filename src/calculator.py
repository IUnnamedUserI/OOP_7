#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите простейший калькулятор, состоящий из двух текстовых полей, куда
пользователь вводит числа, и четырех кнопок "+", "-", "*", "/". Результат
вычисления должен отображаться в метке. Если арифметическое действие выполнить
невозможно (например, если были введены буквы, а не числа), то в метке должно
появляться слово "ошибка".
"""

from tkinter import Tk, Entry, Frame, Button, Label, LEFT


def calculate(operation):
    """
    Выполняет арифметическую операцию над числами из текстовых полей.
    Результат отображается в метке.
    """
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "ошибка"
            else:
                result = num1 / num2

        result_label.config(text=f"Результат: {result}")

    except ValueError:
        result_label.config(text="ошибка")


def main():
    """Основная функция для создания графического интерфейса."""
    global entry1, entry2, result_label

    root = Tk()
    root.title("Калькулятор")
    root.geometry("250x200")

    entry1 = Entry(root, width=20)
    entry1.pack(pady=5)

    entry2 = Entry(root, width=20)
    entry2.pack(pady=5)

    button_frame1 = Frame(root)
    button_frame1.pack()

    button_add = Button(button_frame1, text="+", width=10,
                        command=lambda: calculate('+'))
    button_add.pack(side=LEFT, padx=5, pady=5)

    button_sub = Button(button_frame1, text="-", width=10,
                        command=lambda: calculate('-'))
    button_sub.pack(side=LEFT, padx=5, pady=5)

    button_frame2 = Frame(root)
    button_frame2.pack()

    button_mul = Button(button_frame2, text="*", width=10,
                        command=lambda: calculate('*'))
    button_mul.pack(side=LEFT, padx=5, pady=5)

    button_div = Button(button_frame2, text="/", width=10,
                        command=lambda: calculate('/'))
    button_div.pack(side=LEFT, padx=5, pady=5)

    result_label = Label(root, text="Результат: ")
    result_label.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
