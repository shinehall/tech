#coding=utf-8

#迭代字符串
s = 'hello world'

#通过string定义的迭代器进行迭代
striter = s.__iter__()
print('use next func: ' + striter.__next__())
for i in striter:
    print(i)
print('test str over!')
#通过内置函数iter和next进行迭代
baseiter = iter(s)
print('use base func: ' + next(baseiter))
print('use iter\'s func: ' + baseiter.__next__())
for i in baseiter:
    print(i)
