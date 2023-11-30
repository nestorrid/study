# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : data_structures.py
# @Date         : 2023/11/5 02:10
#
# @Description  :
#

letters = ['a', 'b', 'c', 'd', 'e']
matrix = [[0, 1], [1, 2], [3, 4], [5, 6]]
zeros = [0] * 100
combined = letters + zeros
print(combined)
numbers = list(range(20))
characters = list('hello world')
print(characters)

one, two, three = [1, 2, 3]
five, six, *others = [5, 6, 7, 8, 9, 10]
print(one, two, three, five, six)
print(others)

# 使用枚举器遍历
for index, letter in enumerate(letters):
    print(index, letter)

letters.append('d')
print(letters)
letters.insert(0, '-')
print(letters)
letters.pop(0)  # 删除指定下标
print(letters)
letters.pop()  # 删除最后一个
print(letters)
letters += ['a', 'a', 'a']
print(letters)
letters.remove('a')  # 仅删除第一个匹配项
print(letters)
del letters[-3:]  # 删除最后三项
print(letters)

print(letters.index('c'))

if 'f' in letters:
    print(letters.index('f'))

letters.clear()  # 清空列表
print(letters)

nums = [2, 8, 1, 7, 15, 33, 12]
print(nums.sort())  # 列表的sort方法没有返回值,而是直接将列表本身排序
print(nums)
print(sorted(nums, reverse=True))  # sorted()方法创建一个新的排序列表,原列表保持不变
print(nums)

items = [
    ('a', 10),
    ('f', 8),
    ('c', 12),
    ('e', 115),
    ('b', 3),
]


def sort_by_tag(item):
    return item[0]


def sort_by_price(item):
    return item[1]


items.sort(key=sort_by_tag)
print(items)
items.sort(key=sort_by_price)
print(items)

# 通过lambda简化代码
items.sort(key=lambda item: item[0])
print(items)

# map函数结合lambda处理列表
# item 每次迭代要操作的对象
# item[0] 要返回的值,也可以对这个值进行其他操作,如 `f"tag-{item[0]}"`
tags = list(map(lambda item: f"tag-{item[0]}", items))  # 对迭代器对象中的所有元素执行lambda给定的操作
print(tags)

# filter过滤器函数
filtered_items = list(filter(lambda item: item[1] > 50, items))
print(filtered_items)

# 生成器
tags = [item[0] for item in items]
print(tags)
filtered_items = [item[1] for item in items if item[1] > 10]
print(filtered_items)

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print(list(zip(list1, list2)))
print(list(zip(list2, list1)))
print(list(zip('zxcvbn', list2, list1)))

# Stack 栈结构, LIFO(Last In First Out)后进先出
stack_list = [0]
print(stack_list)
stack_list.append(1)
stack_list.append(2)
last = stack_list.pop()
print(last, stack_list)
last = stack_list.pop()
print(last, stack_list)

# Queue 队列, FIFO(First In First Out)先进先出
# list对象在进行pop操作时直接将最后一个元素移出列表, 操作复杂度为O(1)
# 但是队列操作是将列表的第一个元素移出, 由于列表存在index, 所有元素的index属性都需要变动
# 因此list对象的popleft()操作的执行效率会随着列表中元素数量的增加而增加,即复杂度为O(n)
# 为了提高队列的执行效率, 可以通过collections.deque来进行队列操作
from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
print(queue.popleft(), queue)

# tuple 元组, 不可变的元素列表
t = 1, 2  # 多个值默认直接封装为元组, 经常用于返回多个值的场景, 如: return result1, result2
t = 1,  # 仅包含一个值, 但是通过添加一个`,`显示声明将其封装为元组
t = ()  # 显示声明一个空的元组
t = tuple([1, 2])  # 将列表对象转为元组

# 利用元组进行数值交换
a, b = 0, 1
a, b = (b, a)  # 不加括号也可以, a,b = b,a
print(a, b)

# array, python内置数据类型, 与list操作相同, 区别在于array中的所有元素类型相同, 在大数据量的操作中效率高于list
from array import array

nums = array('i', [1, 2, 3, 4])
print(nums)
# nums.append(1.5) TypeError: 'float' object cannot be interpreted as an integer

# set, 无序集合, 元素唯一
nums = [1, 1, 2, 2, 3, 3, 4, 4]
unique = set(nums)
print(unique)

first_set = {'a', 'e', 'i', 'o', 'u'}
second_set = {'b', 'n', 'j', 'u', 'k'}

print(first_set | second_set)  # 在任意一个集合中存在的元素, 即两个集合的并集
print(first_set & second_set)  # 同时存在于两个集合的元素, 即两个集合的交集

# 两个集合的差集, 在第一个集合中去除第二个集合中所包含的元素
print(first_set - second_set)  # {'i', 'o', 'a', 'e'}
print(second_set - first_set)  # {'b', 'k', 'n', 'j'}

print(first_set ^ second_set)  # 对称差, 两个集合的合集 - 两个集合的交集

# dictionary, 词典, 键值对对象
empty_dict = {}
point = {"x": 1, "y": 2}
point = dict(x=2, y=3)
print(point["x"])
point["z"] = 100
print(point)

if 'key' in point:
    print(point['key'])  # key不存在, 该行代码不会执行

del point['z']
print(point)

for key in point:
    print(point[key])

for item in point.items():
    print(item)

# generator, 生成器, 可以进行迭代的对象, 每次迭代获取下一个元素,直至遍历完成
# 生成器最大的优势在于节省系统空间, 对于list来说,所有的元素都需要保存在内存中, 当list非常大时就会十分占用系统资源
# 但是生成器仅仅是一个获取下一个元素的代码段, 并不实际储存元素, 因此其空间占用是固定的
from sys import getsizeof

list1 = [x for x in range(10)]
list2 = [x for x in range(100)]
list3 = [x for x in range(100000)]
print("size of list:", getsizeof(list1), getsizeof(list2), getsizeof(list3))

# 在()中使用生成器表达式获得的是一个generator
gen1 = (x for x in range(10))
gen2 = (x for x in range(100))
gen3 = (x for x in range(10000))
print("size of generator:", getsizeof(gen1), getsizeof(gen2), getsizeof(gen3))

# exercise, 找出出现次数最多的字符
sentence = 'This is a common interview question'

characters = {}
for c in sentence:
    if c in characters:
        characters[c] += 1
    else:
        characters[c] = 1

print(characters)

count = {}

for k, v in characters.items():
    k = '空格' if k == ' ' else k
    if v in count:
        count[v] += k + " "
    else:
        count[v] = k + " "

keys = count.keys()
print(count[sorted(keys).pop()])

print(sorted(characters.items(), key=lambda item: item[1]).pop())
