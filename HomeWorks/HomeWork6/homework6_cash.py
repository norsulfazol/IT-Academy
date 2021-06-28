#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############
# Main module #
###############

from decimal import Decimal
from homework6_str import is_decimal

_DENOM = (500, 200, 100, 50, 20, 10, 5, 2, 1, .5, .2, .1, .05, .02, .01)

_HUMAN_DENOM_FORMAT = {(500, 200, 100, 50, 20, 10, 5): '{amount} куп. по {denom} рублей',
                       (2,): '{amount} мон. по {denom} рубля',
                       (1,): '{amount} мон. по {denom} рублю',
                       (.5, .2, .1, .05): '{amount} мон. по {denom} копеек',
                       (.02, .01): '{amount} мон. по {denom} копейки'}


def get_denominations(money_amount, idx=0, result=None):
    """
    Forms a list with the number and denominations of banknotes and coins.

    :param money_amount: Decimal
    :param idx: int
    :param result: list of str
    :return: list of str
    """
    if result is None:
        result = []
    quotient, remainder = divmod(money_amount, round(Decimal(_DENOM[idx]), 2))
    if quotient:
        for k, v in _HUMAN_DENOM_FORMAT.items():
            if _DENOM[idx] in k:
                result.append(v.format(amount=quotient,
                                       denom=round(Decimal(_DENOM[idx] * (100 if _DENOM[idx] < 1 else 1)), 0)))
                break
    return get_denominations(remainder, idx + 1, result) if remainder else result


if __name__ == '__main__':
    title = 'Расчёт размера сдачи и номиналов купюр/монет для сдачи'
    print('-' * len(title), title, '-' * len(title), sep='\n')
    params = {'price': 'Цена товара/услуги', 'received': 'Получена сумма'}
    for k in params:
        while True:
            value = input(f'{params[k]} (<рубли>.<копейки>): ').replace(' ', '').replace('-', '')
            if is_decimal(value):
                params[k] = round(Decimal(value), 2)
                break
            print('Невалидное значение!')
    odd_money = params['received'] - params['price']
    title = f'{"Сдача" if odd_money > 0 else "Недополучена сумма"} (<рубли>.<копейки>): {str(odd_money)}' if odd_money \
        else 'Без сдачи.'
    print('-' * len(title), title, sep='\n')
    if odd_money > 0:
        print('-' * len(title))
        for denom in get_denominations(odd_money):
            print(f'=> {denom}')
    input('\nНажмите клавишу <Enter>, чтобы завершить программу ...')
