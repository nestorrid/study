# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : csv_file.py
# @Date         : 2023/11/5 18:14
#
# @Description  :
#

import csv

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "age"])
    writer.writerow([1, "a", 3])
    writer.writerow([2, "b", 5])
    writer.writerow([3, "c", 6])

with open('data.csv') as file:
    reader = csv.reader(file)
    # csv读取器每次读取一行都会把文件指针下移,
    # 通过list()函数进行读取便是直接读取全部文件,文件指针已经移至末尾,就会使后续的for语句失效
    # print(list(reader))
    for row in reader:
        print(row)
