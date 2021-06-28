#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, time

HUMAN_TIME_UM = {'hour_nom': ('час', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять',
                              'одиннадцать', 'двенадцать'),
                 'hour_gen': ('первого', 'второго', 'третьего', 'четвёртого', 'пятого', 'шестого', 'седьмого',
                              'восьмого', 'девятого', 'десятого', 'одиннадцатого', 'двенадцатого'),
                 'minute_nom': ('', 'одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять',
                                'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', '', 'шестнадцать',
                                'семнадцать', 'восемнадцать', 'девятнадцать'),
                 'minute_gen': ('', 'одной', 'двух', 'трёх', 'четырёх', 'пяти', 'шести', 'семи', 'восьми', 'девяти',
                                'десяти', 'одиннадцати', 'двенадцати', 'тринадцати', 'четырнадцати', '', 'шестнадцати',
                                'семнадцати', 'восемнадцати', 'девятнадцати', 'двадцати')}

HUMAN_TIME_FORMAT = {(((1,),), ((1,),)): 'полночь',
                     (((1, 2), (13, 14)), ((1,),)): 'час ровно',
                     (((2, 5), (14, 17)), ((1,),)): '{hn} часа ровно',
                     (((5, 13), (17, 24)), ((1,),)): '{hn} часов ровно',
                     (((24,),), ((1, 2),)): '{mn} минута {hg}',
                     (((24,),), ((2, 5),)): '{mn} минуты {hg}',
                     (((24,),), ((5, 15), (16, 20))): '{mn} минут {hg}',
                     (((24,),), ((21, 22),)): 'двадцать {mn} минута {hg}',
                     (((24,),), ((22, 25),)): 'двадцать {mn} минуты {hg}',
                     (((24,),), ((20, 21), (25, 30))): 'двадцать {mn} минут {hg}',
                     (((24,),), ((31, 32),)): 'тридцать {mn} минута {hg}',
                     (((24,),), ((32, 35),)): 'тридцать {mn} минуты {hg}',
                     (((24,),), ((35, 40),)): 'тридцать {mn} минут {hg}',
                     (((24,),), ((15, 16),)): 'четверть {hg}',
                     (((24,),), ((30, 31),)): 'половина {hg}',
                     (((23, 24),), ((40, 45), (46, 59))): 'без {mg} минут полночь',
                     (((23, 24),), ((59, 60),)): 'без {mg} минуты полночь',
                     (((23, 24),), ((45, 46),)): 'без четверти полночь',
                     (((23,),), ((40, 45), (46, 59))): 'без {mg} минут {hn}',
                     (((23,),), ((59, 60),)): 'без {mg} минуты {hn}',
                     (((23,),), ((45, 46),)): 'без четверти {hn}'}


def time2hformat(dt_obj):
    """ Преобразование объекта времени в строку в "человеческом" формате.

    :param dt_obj: datetime.time or datetime.datetime object
    :return: formatted string
    """
    # поиск формата времени
    for k in HUMAN_TIME_FORMAT:
        # проверка на вхождение в диапазоны
        if all([any([dt_obj.hour in range(*ht) for ht in k[0]]),
                any([dt_obj.minute in range(*mt) for mt in k[1]])]):
            # корректировка количества часов и минут
            h = dt_obj.hour + (1 if dt_obj.hour < 12 else -11) - (1 if dt_obj.minute else 2)
            m = dt_obj.minute if dt_obj.minute < 40 else 60 - dt_obj.minute
            # возврат отформатированной строки с подставленными значениями
            return HUMAN_TIME_FORMAT[k].format(
                hn=HUMAN_TIME_UM['hour_nom'][h],
                hg=HUMAN_TIME_UM['hour_gen'][h],
                mn=HUMAN_TIME_UM['minute_nom'][m if m < 20 else m - (20 if m < 30 else 30)],
                mg='' if dt_obj.minute < 40 else HUMAN_TIME_UM['minute_gen'][m]).replace('  ', ' ')
    return ''


def test_time2hformat():
    for h in range(24):
        for m in range(60):
            print(f'{h}:{m} - {time2hformat(time(h, m))}')


def what_time_is_it():
    title = 'Угадайте текущее время.'
    print('-' * len(title), title, '-' * len(title), sep='\n')
    while True:
        try:
            dt_obj = datetime.strptime(
                input('Введите время в формате "ЧЧ:ММ", где ЧЧ - количество часов, ММ - количество минут: ').replace(
                    ' ', ''), '%H:%M')
            break
        except ValueError:
            print('Необходимо ввести время в указанном формате!')
    curr_dt_obj = datetime.now()
    title = f'Текущее время "{curr_dt_obj.strftime("%H:%M")}" - {time2hformat(curr_dt_obj).capitalize()}.'
    print('-' * len(title), title, sep='\n')
    print(f'Ваше время "{dt_obj.strftime("%H:%M")}" - {time2hformat(dt_obj).capitalize()}.')
    print(
        f'{"" if time(dt_obj.hour, dt_obj.minute) == time(curr_dt_obj.hour, curr_dt_obj.minute) else "не "}угадали!'.capitalize())
    input('\nНажмите клавишу <Enter>, чтобы завершить программу ...')


if __name__ == '__main__':
    # test_time2hformat()
    what_time_is_it()
