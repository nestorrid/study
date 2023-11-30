# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : random_values.py
# @Date         : 2023/11/5 19:04
#
# @Description  :
#

import random
import string

print(random.random())
print(random.random())
print(random.random())

print(random.randint(1, 10))
print(random.randint(1, 10))

print(random.choice([1, 2, 3, 4, 5]))
print(random.choice([1, 2, 3, 4, 5]))

print(random.choices([1, 2, 3, 4, 5], k=3))
print(random.choices([1, 2, 3, 4, 5], k=3))

# random password
pwd = "".join(random.choices(string.ascii_letters + string.digits, k=16))
print(pwd)
pwd = "".join(random.choices(string.ascii_letters + string.digits, k=16))
print(pwd)
