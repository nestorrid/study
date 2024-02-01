# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : command_line_args.py
# @Date         : 2023/11/5 19:58
#
# @Description  :
#
import sys

"""
> python command_line_args.py -a -b
> ['command_line_args.py', '-a', '-b']
"""
print(sys.argv)  # 第一个命令行参数始终是当前执行的py文件

if len(sys.argv) == 1:
    print("use as least one argument.")
else:
    print(sys.argv[1])
