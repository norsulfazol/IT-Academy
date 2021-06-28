#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from decimal import Decimal, InvalidOperation
from functools import reduce


def is_decimal(string):
    """ Проверка строки на возможность её преобразования в объект Decimal.
    """
    if string.isdecimal():
        return True
    try:
        Decimal(string)
        return True
    except InvalidOperation:
        return False


def print_warning(warning_str, delay=1.5):
    """ Вывод предупреждения с задержкой на указанное время (сек.) и с возвратом каретки в начало строки.
    """
    print(f'\r{warning_str}', end='')
    sleep(delay)
    print('\r', ' ' * len(warning_str), end='\r')  # - костыль ("затирание" строки)


def calc_deposit():
    # первоначальные параметры
    params = {'start_balance': {'title': 'Первоначальный сумма (BYN', 'default_value': Decimal(0)},
              'deposit_term': {'title': 'Срок действия депозита (мес.', 'default_value': 60},
              'percent_per_annum': {'title': 'Процентная ставка [годовых] (%', 'default_value': Decimal(15)},
              'prec': {'title': 'Округление результата (зн. после запятой', 'default_value': 2}}
    # вывод заголовка
    title = 'Расчёт итоговой суммы депозита за указанный период (с ежемесячной капитализацией)'
    print('-' * len(title), title, '-' * len(title), sep='\n')
    # пользовательский интерфейс (запрос и изменение параметров)
    for item in params:
        while True:
            # запрос ввода параметра
            new_value = input(f'{params[item]["title"]}, по умолчанию - {params[item]["default_value"]}): ')
            # проверка введённой строки
            if not new_value:
                params[item] = params[item]['default_value']
                break
            if isinstance(params[item]['default_value'], Decimal):
                if is_decimal(new_value):
                    params[item] = Decimal(new_value)
                    break
                print_warning('Необходимо указать число!')
            elif isinstance(params[item]['default_value'], int):
                if new_value.isdigit():
                    params[item] = int(new_value)
                    break
                print_warning('Необходимо указать целое число!')
    # собственно сам расчёт
    final_balance = reduce(lambda x, y: x + x * params['percent_per_annum'] / Decimal(100) / Decimal(12),
                           range(params['deposit_term']), params['start_balance'])
    # вывод результата
    title = f'ИТОГО: {final_balance:.{params["prec"]}f} BYN'
    print('-' * len(title), title, sep='\n')


if __name__ == '__main__':
    calc_deposit()
