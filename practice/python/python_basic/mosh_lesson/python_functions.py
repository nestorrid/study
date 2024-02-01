# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : python_functions.py
# @Date         : 2023/11/4 23:36
#
# @Description  :
#

def greeting():
    print("Hello")


greeting()


def sum_list(*numbers):
    s = 0
    for num in numbers:
        s += num
    return s


print(sum_list(1, 2, 3, 4, 5))


def print_dict(**kwargs):
    print(kwargs)


print_dict(id=1, name="Nestor", age=35)


def fizz_buzz(num):
    result = ""
    if num % 3 == 0:
        result += "fizz"
    if num % 5 == 0:
        result += "buzz"

    return result if result else num


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(7))
print(fizz_buzz(15))
