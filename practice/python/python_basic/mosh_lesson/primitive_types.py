# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : lesson1.py
# @Date         : 2023/11/4 21:14
#
# @Description  :
#
import math

students_count = 1000  # 数字
rating = 4.99
is_published = True
course_name = "Python Programming"

print(len(course_name))  # 18
print(course_name[0])  # P
print(course_name[-1])  # g
print(course_name[0:3])  # Pyt, 从下标为0开始,取3个
print(course_name[:3])  # Pyt, 从字符串起始位置开始, 取3个
print(course_name[0:])  # Python Programming, 从字符串开始取到结尾

# 常用转义字符
# \"
# \'
# \\
# \n 换行

first = "张"
last = "三"
full_name = first + " " + last
full_name_2 = f"{first} {last}"
print(full_name)
print(full_name_2)

test_string = "    somE teSt stRing   "
print(test_string)
print(test_string.upper())
print(test_string.lower())
print(test_string.title())
print(test_string.strip())
print(test_string.lstrip())
print(test_string.rstrip())
print("e" in test_string)
print("aaa" not in test_string)

print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

print(round(2.8))  # 3
print(round(2.1))  # 2

print(math.floor(2.1))  # 2
print(math.floor(2.8))  # 2

print(math.ceil(2.1))  # 3
print(math.ceil(2.8))  # 3

input_num = input("x: ")
print(type(input_num))
print(type(int(input_num)))

y = int(input_num) + 1
print(y)
