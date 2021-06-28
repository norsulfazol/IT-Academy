#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_ranges(int_list):
    result = [[str(int_list[0])]]
    for i, e in enumerate(int_list[1:]):
        if e == int_list[i] + 1:
            result[-1] = [result[-1][0], str(e)]
        else:
            result.append([str(e)])
    return ', '.join(['-'.join(i) for i in result])


if __name__ == '__main__':
    title = 'Проверка функции "сворачивания" отсортированного списка уникальных целых чисел'
    print('-' * len(title), title, '-' * len(title), sep='\n')
    int_list = sorted(random.sample(range(100), 20))
    print(f'int_list = {int_list}')
    print(f'result = "{get_ranges(int_list)}"')

    title = 'FizzBuzz'
    print('', '-' * len(title), title, '-' * len(title), sep='\n')
    print(', '.join([str(i) if all([i % 3, i % 5]) else f'{"" if i % 3 else "Fizz"}{"" if i % 5 else "Buzz"}' for i in
                     range(1, 101)]))

    # from habr
    # ', '.join([['Fizz', '', ''][i % 3] + ['Buzz', '', '', '', ''][i % 5] or i for i in range(1, 101)])
