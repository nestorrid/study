# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : handle_exceptions.py
# @Date         : 2023/11/5 14:08
#
# @Description  :
#

# 异常处理格式
try:
    age = int(input("Age: "))
except ValueError as e:
    print("You need to enter a valid number for age.")
    print(e)
else:
    print("no exceptions were thrown.")

print("Done!")

# 同时处理多个异常
try:
    num = int(input("Number: "))
    r = 10 / num
except (ValueError, ZeroDivisionError):
    print("Invalid number.")
else:
    print("No exceptions were thrown.")

# finally
try:
    file = open("handle_exceptions.py")
except IOError:
    print("File not found")
else:
    print("File successfully")
finally:
    file.close()


# 抛出异常
def calculate_xfactor(arg):
    if arg <= 0:
        raise ValueError("age cannot be 0 or less.")
    return 10 / arg


try:
    calculate_xfactor(0)
except ValueError as e:
    print(e)

# 在方法中抛出异常会在一定程度上影响代码的运行效率
# 在针对用户量或业务量较小, 对性能要求不高的程序时没有太大影响
# 反之则存在比较大的性能隐患, 如果能够在不抛出异常的情况下达到相同的作用不建议抛出异常
from timeit import timeit

code1 = """
def calculate_xfactor(arg):
    if arg <= 0:
        raise ValueError("age cannot be 0 or less.")
    return 10 / arg


try:
    calculate_xfactor(0)
except ValueError as e:
    pass
"""

code2 = """
def calculate_xfactor(arg):
    if arg <= 0:
        return None
    return 10 / arg


result = calculate_xfactor(0)
if not result:
    pass
"""

# 两段作用相同的代码, 在执行10000次的测试条件下效率达到4倍差距
print("code1", timeit(code1, number=10000))  # 0.0037266251165419817
print("code2", timeit(code2, number=10000))  # 0.0009943749755620956
