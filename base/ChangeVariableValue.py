#coding=utf-8

a = {'keyOne' : 1, 'keyTwo' : 2}
print(a.get('keyOne'))
b = a
b['keyOne'] = 2
print(a['keyOne'])

s = 'hello world'
yiter = s.__iter__()
yiter.__next__()
miter = iter(s)
print(miter.__next__())