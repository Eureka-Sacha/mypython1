# -*- coding: utf-8 -*-
# 如使用中文必须设置编码为UTF-8
__author__ = '奎'
# print 方法,没啥好说的
print 'hello world'
print 'hello', 'world'
print 100 + 100
# 对象输出
a = 250
print(a)
# 多行输出
print """hello
world
"""
# 或门
print True or False
# 与门
print True and False
# 非门
print not True
# None 等价于Null
print None


# list集合
# list里面的元素的数据类型也可以不同
list = ['a', 'b', 'c']
print list
# 元素个数
print len(list)
# 和JAVA一样使用索引获取元素  从0开始
print list[0]
# 输入-1直接获取最后一个元素  -2,-3,-4 也是可行的
print list[-1]
# 向集合中追加元素
list.append('d')
print list
# 指定索引位置添加元素
list.insert(1, '2')
print list
# 删除指定索引位置的元素  不指定删除最后一个
list.pop(1)
print list
# tuple集合 和list差不多 只是创建完成后无法修改 无法追加
tuple = ('a', 'b', 'c')
print tuple


# if判断    没啥可说的注意缩进
age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'

# for 循环
# 第一种 :直接迭代集合
for x in list:
    print x
# 第二种 :循环数列 其实和第一种方法没本质区别,都是迭代
for x in range(1, 500, 50):
    print x
# 顺便记一下 range(start,stop,step) 方法, 看了就懂了
print range(0, 1000, 100)

# while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum
# 控制台输入
print raw_input('input something to exit:')