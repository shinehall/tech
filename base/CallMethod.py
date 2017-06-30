#coding=utf-8

class Computer(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __call__(self, comptype):
        if comptype == 'add':
            return self.x + self.y
        elif comptype == 'mult':
            return self.x * self.y

com1 = Computer(2, 3)
rs = com1('add')
print('get result: ' + str(rs))