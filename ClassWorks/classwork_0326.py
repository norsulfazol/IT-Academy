#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def sorted_alt(collection, key=None, reverse=False):
    """ Альтернативная сортировка.
    """
    collection = list(collection)
    min_args = {} if key is None else {'key': key}  # in version < 3.8: min(iter, key != None)
    collection = [collection.pop(collection.index(min(collection, **min_args))) for i in range(len(collection))]
    return collection[::-1] if reverse else collection


def infinity_cycle_for():
    """ Бесконечный цикл for.
    """
    x = [0]
    for i in x:
        x += [x[-1] + 1]
        print(i)


def list_manipulation():
    # исходная строка
    val = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
    # замен строк числами с удаление дубликатов чисел, сортировка списка
    val = sorted([{'one': 1,
                   'two': 2,
                   'four': 4,
                   'five': 5,
                   'eight': 8,
                   'ten': 10,
                   'eleven': 11,
                   'thirteen': 13,
                   'seventeen': 17,
                   'nineteen': 19
                   }.get(val.strip(), 0) for val in set(val.lower().split())])
    print(f'Список: {val}')
    print(f'Сумма нечётных чисел: {sum([val for val in val if val % 2])}')
    print('Суммы и произведения смежных чисел:')
    while len(val) > 1:
        print(
            f'{val[0]}+{val[1]}={val.pop(0) + val[0]}' if len(val) % 2 else f'{val[0]}*{val[1]}={val.pop(0) * val[0]}')


if __name__ == '__main__':
    title = 'Проверка альтернативной сортировки чисел и её сравнение с оригинальной сортировкой'
    print('-' * len(title), title, '-' * len(title), sep='\n')
    ex_list = list(range(500))
    random.shuffle(ex_list)
    print('ex_list =', ex_list)
    print('\nsorted =', sorted(ex_list, reverse=False))
    print('\nsorted_alt =', sorted_alt(ex_list))
    print('\nsorted_alt_reverse =', sorted_alt(ex_list, reverse=True))

    title = 'Проверка альтернативной сортировки строк и её сравнение с оригинальной сортировкой'
    print('', '-' * len(title), title, '-' * len(title), sep='\n')
    ex_list = ['test', 'TEst', 'dfsfs', 'qqa', 'gfbgfb',
               'зелёной', 'синевой', 'краснеется', 'чепуржисть',
               'белеет', 'чернотой', 'сиреневый', 'желток']
    random.shuffle(ex_list)
    print('ex_list =', ex_list)
    print('\nsorted =', sorted(ex_list, key=str.lower, reverse=False))
    print('\nsorted_alt =', sorted_alt(ex_list, key=str.lower, reverse=False))
    print('\nsorted_alt_reverse =', sorted_alt(ex_list, key=str.lower, reverse=True))

    # title = 'Проверка бесконечного цикла for'
    # print('', '-' * len(title), title, '-' * len(title), sep='\n')
    # infinity_cycle_for()

    title = 'Проверка функции манипуляции со списком'
    print('', '-' * len(title), title, '(с использованием одной переменной)', '-' * len(title), sep='\n')
    list_manipulation()
