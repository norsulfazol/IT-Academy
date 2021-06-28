##########################
# Math operations module #
##########################

MATH_FUNC = {'/': 'quot', '*': 'prod', '-': 'diff', '+': 'sum'}


def get_quot(number_left, number_right):
    """
    Returns the quotient of numbers.

    :param number_left: int or float
    :param number_right: int or float
    :return: int or float
    """
    return number_left / number_right


def get_prod(number_left, number_right):
    """
    Returns the product of numbers.

    :param number_left: int or float
    :param number_right: int or float
    :return: int or float
    """
    return number_left * number_right


def get_diff(number_left, number_right):
    """
    Returns the difference of numbers.

    :param number_left: int or float
    :param number_right: int or float
    :return: int or float
    """
    return number_left - number_right


def get_sum(number_left, number_right):
    """
    Returns the sum of numbers.

    :param number_left: int or float
    :param number_right: int or float
    :return: int or float
    """
    return number_left + number_right
