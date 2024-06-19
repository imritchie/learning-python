import math


def calculate_and_print(num, calculator, formatter):
    result = calculator(num)
    formatter(num, result)


def calculate_square(num):
    return math.pow(num, 2)


def calculate_cube(num):
    return math.pow(num, 3)


def calculate_plus_10(num):
    return num + 10


def format_func(num, result):
    print(f'''
        | 打印： | {num}
        > 计算结果 ： {result}
    ''')


calculate_and_print(7, calculate_plus_10, format_func)
