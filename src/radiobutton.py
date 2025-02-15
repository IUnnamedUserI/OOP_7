#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Виджеты Radiobatton и Checkbutton поддерживают большинство свойств
оформления внешнего вида, которые есть у других элементов графического
интерфейса. При этом у Radiobutton есть особое свойство indicatoron.
По-умолчанию он равен единице, в этом случае радиокнопка выглядит как
нормальная радиокнопка. Однако если присвоить этой опции ноль, то виджет
Radiobutton становится похожим на обычную кнопку по внешнему виду. Но не по
смыслу. Напишите программу, в которой имеется несколько объединенных в группу
радиокнопок, индикатор которых выключен (indicatoron=0). Если какая-нибудь
кнопка включается, то в метке должна отображаться соответствующая ей
информация. Обычных кнопок в окне быть не должно.
"""

from tkinter import Tk, Frame, Radiobutton, Label, IntVar, W, LEFT, RIGHT


def update_label():
    """
    Обновляет метку в зависимости от выбранной радиокнопки.
    """
    selected_option = var.get()
    if selected_option == 1:
        label.config(text="+7 (912) 345-67-89")
    elif selected_option == 2:
        label.config(text="+7 (923) 456-78-90")
    elif selected_option == 3:
        label.config(text="+7 (934) 567-89-01")
    elif selected_option == 4:
        label.config(text="+7 (945) 678-90-12")


def main():
    """Основная функция для создания графического интерфейса."""
    global var, label

    root = Tk()
    root.title("Радиокнопки без индикатора")
    root.geometry("400x200")

    radio_frame = Frame(root)
    radio_frame.pack(side=LEFT, padx=10, pady=10)

    var = IntVar()

    radio1 = Radiobutton(
        radio_frame, text="Алексей", variable=var, value=1,
        indicatoron=0, command=update_label, width=10, height=2
    )
    radio1.pack(anchor=W, pady=0)

    radio2 = Radiobutton(
        radio_frame, text="Мария", variable=var, value=2,
        indicatoron=0, command=update_label, width=10, height=2
    )
    radio2.pack(anchor=W, pady=0)

    radio3 = Radiobutton(
        radio_frame, text="Дмитрий", variable=var, value=3,
        indicatoron=0, command=update_label, width=10, height=2
    )
    radio3.pack(anchor=W, pady=0)

    radio4 = Radiobutton(
        radio_frame, text="Анна", variable=var, value=4,
        indicatoron=0, command=update_label, width=10, height=2
    )
    radio4.pack(anchor=W, pady=0)

    info_frame = Frame(root)
    info_frame.pack(side=RIGHT, padx=10, pady=10)

    label = Label(info_frame, text="", font=("Arial", 12))
    label.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
