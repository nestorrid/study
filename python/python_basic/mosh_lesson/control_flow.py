# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : control_flow.py
# @Date         : 2023/11/4 22:18
#
# @Description  :
#

temperature = 35
if temperature > 30:
    print("It's hot")
elif temperature > 20:
    print("It's warm")
else:
    print("It's cold")

print("Done")

age = 20
# if age >= 18:
#     message = "已成年"
# else:
#     message = "未成年"

message = "已成年" if age >= 18 else "未成年"

print(message)

if 18 <= age < 60:
    print("approved")
else:
    print("rejected")

flag = False
for i in range(5):
    print(i)
    if flag:
        break  # 跳出for循环的代码块
else:  # 因为else和for在同一个代码块内,如果break语句执行,则else不会被执行
    print("print 5 times")  # 仅当for循环完整运行之后才会执行该代码段
