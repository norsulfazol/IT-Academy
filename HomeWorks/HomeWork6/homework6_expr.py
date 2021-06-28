#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############
# Main module #
###############

import homework6_math as math
from homework6_str import is_int_or_float, from_string


def replace_pairs(expr):
    """
    Replaces pairs of mathematical operations.

    :param expr: str
    :return: str
    """
    for k, v in {'++': '+', '--': '+', '+-': '-', '-+': '-', '*+': '*', '/+': '/'}.items():
        expr = expr.replace(k, v)
    return expr


def get_number_str(expr, idx_math_oper, step=-1):
    """
    Returns the substring of a number to the left or right of a mathematical operator in an expression.
    It also returns the index of the beginning or end of a substring of a number.

    :param expr: str
    :param idx_math_oper: int
    :param step: int (-1 or 1)
    :return: tuple(str, int)
    """
    result = ''
    idx = idx_math_oper + step
    while idx in range(len(expr)) and expr[idx] not in '/*+':
        if all([expr[idx] == '-', any([all([step == -1, idx]), all([step == 1, idx != idx_math_oper + step])])]):
            break
        result += expr[idx]
        idx += step
    return result[::step], idx if step == 1 else idx + 1


def calc_math_subexpr(expr):
    """
    Calculates a mathematical subexpression without parentheses, passed as a string.

    :param expr: str
    :return: str
    """
    if is_int_or_float(expr):
        return expr
    for math_oper_group in ('/*', '-+'):
        for idx_math_oper, math_oper in enumerate(expr):
            if all([idx_math_oper, math_oper in math_oper_group]):
                number_left, idx_subexpr_start = get_number_str(expr, idx_math_oper)
                number_right, idx_subexpr_end = get_number_str(expr, idx_math_oper, 1)
                math_func = getattr(math, f'get_{math.MATH_FUNC[math_oper]}')
                return calc_math_subexpr(replace_pairs(expr.replace(expr[idx_subexpr_start:idx_subexpr_end],
                                                                    str(math_func(from_string(number_left),
                                                                                  from_string(number_right))))))


def calc_math_expr(expr):
    """
    Calculates a mathematical expression with parentheses, passed as a string.

    :param expr: str
    :return: int or float
    """
    if is_int_or_float(expr):
        return from_string(expr)
    idx_open_par = expr.rfind('(') + 1
    if idx_open_par:
        idx_close_par = expr.find(')', idx_open_par)
        return calc_math_expr(replace_pairs(expr.replace(expr[idx_open_par - 1:idx_close_par + 1],
                                                         calc_math_subexpr(expr[idx_open_par:idx_close_par]))))
    return calc_math_subexpr(expr)


if __name__ == '__main__':
    title = 'Calculating a mathematical expression'
    print('-' * len(title), title, '-' * len(title), sep='\n')
    while True:
        try:
            expr = input('Enter math expression: ').replace(' ', '')
            exec(expr)
            break
        except Exception:
            print('Error: Invalid math expression!')
    title = f'Result: {expr} = {calc_math_expr(expr)}'
    print('-' * len(title), title, sep='\n')
    print(f'Check: eval("{expr}") = {eval(expr)}')
    input('\nPress <Enter> key to complete the program ...')
