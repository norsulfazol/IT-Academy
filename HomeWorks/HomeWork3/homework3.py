#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def full_replace(string, substr_srch, substr_new):
    """
    Replaces all occurrences of a substring in a string with a new substring and returns the formatted string.

    :param string: str
    :param substr_srch: str
    :param substr_new: str
    :return: str
    """
    while substr_srch in string:
        string = string.replace(substr_srch, substr_new)
    return string


def get_lines_list(line, line_max_lenght):
    """
    Splits a string into multiple lines that are no longer than the maximum string length and returns a list of strings.

    :param line: str
    :param line_max_lenght: int
    :return: list
    """
    if len(line) <= line_max_lenght:
        return [line]
    result = []
    while line:
        line, next_line = line[:line_max_lenght], line[line_max_lenght:]
        if next_line:
            # если порвали слово
            if all([line[-1].strip(), next_line[0].strip()]):
                line = line.rsplit(' ', 1)
                line, next_line = line[0], f'{line[-1]}{next_line}'
        result.append(line.rstrip())
        line = next_line.lstrip()
    return result


def get_adjusted_lenght_line(line, line_max_lenght):
    """
    Adds spaces between words while the string is less than the maximum length and returns the formatted string.

    :param line: str
    :param line_max_lenght: int
    :return: str
    """
    line = line.split()
    gaps_count = len(line) - 2
    word_idx = 0
    while len(' '.join(line)) < line_max_lenght:
        line[word_idx] += ' '
        word_idx = word_idx + 1 if word_idx < gaps_count else 0
    return ' '.join(line)


def create_formatted_file(file_in, file_out='', encoding_in='utf-8', encoding_out='utf-8'):
    # вывод заголовка
    title = 'Formatting text from a file and saving it to a new file'
    print('-' * len(title), title, '-' * len(title), sep='\n')
    # формирование пути+имени файла-приёмника (если не задано в аргументе)
    file_out = file_out.strip()
    if not file_out:
        file_out = os.path.splitext(file_in)
        file_out = ''.join([file_out[0], '_out', file_out[1]])
    #
    try:
        with open(file_in, 'rt', encoding=encoding_in) as f_in, open(file_out, 'wt', encoding=encoding_out) as f_out:
            # ввод макс. кол-ва символов в строке
            while True:
                try:
                    line_max_lenght = int(
                        input('Enter the maximum line length (> 15): ').replace(' ', ''))
                    if line_max_lenght > 15:
                        break
                    raise ValueError('Integer specified <= 15')
                except ValueError as err:
                    print(f'{err.__class__.__name__}: {str(err).capitalize()}')
            # чтение файла, форматирование текста, запись в файл
            for line in f_in:
                f_out.writelines(f'{get_adjusted_lenght_line(i, line_max_lenght)}\n' for i in
                                 get_lines_list(full_replace(line.strip(), '  ', ' '), line_max_lenght))
            title = f'Formatted text written to file "{file_out}".'
            print('-' * len(title), title, sep='\n')
    except OSError as err:
        print(f'{err.__class__.__name__}: {err.strerror}: {err.filename}')
    input('\nPress <Enter> key to complete the program ...')


if __name__ == '__main__':
    create_formatted_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'text.txt'))
