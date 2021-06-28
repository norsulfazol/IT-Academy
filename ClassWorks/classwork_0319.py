#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def transform_eq_str():
    required_chars = 'xy='  # - символы, которые должны быть в строке уравнения
    # вывод заголовка
    title = f'(в строке уравнения должны присутствовать символы "{required_chars}")'
    print('-' * len(title), 'Преобразование строки уравнения вида "y=5x-10" и расчёт.', title, '-' * len(title),
          sep='\n')
    while True:
        # запрос ввода строки уравнения, очистка от пробелов и перевод в нижний регистр
        eq_str = input('Введите уравнение: ').replace(' ', '').lower()
        # проверка строки уравнения на наличие необходимых символов
        if all([char in eq_str for char in required_chars]):
            break
        print('В строке уравнения отсутствуют необходимые символы!')
    while True:
        try:
            # запрос ввода значения переменной "x", очистка от пробелов и проверка введённой строки
            x = float(input('Введите значение переменной "x": ').replace(' ', ''))
            if math.isfinite(x):
                break
            raise ValueError
        except ValueError:
            print('Необходимо указать число, не представляющее бесконечность!')
    # подстановка значения переменной "x" в формулу
    eq_str = eq_str.replace('x', f'*{"(" if x < 0 else ""}{x}{")" if x < 0 else ""}')
    title = f'Расчёт уравнения "{eq_str}":'
    print('-' * len(title), title, sep='\n')
    # расчёт и вывод результата
    print(f'y = {eval(eq_str.replace("y", "").replace("=", ""))}')
    input('\nНажмите клавишу <Enter>, чтобы завершить программу ...')


if __name__ == '__main__':
    transform_eq_str()
