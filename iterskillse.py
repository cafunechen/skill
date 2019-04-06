'''
生成器
'''
def f():
    print('in f(),1')
    yield 1

    print('in f(),2')
    yield 2

    print('in f(),3')
    yield 3

g = f()
for x in g:
    print(x)
# g.__iter__() id g 可迭代对象
'''实现一个可迭代对象，只用实现__iter__方法就可以'''
class PrimeNumber:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def isPrimeNumber(self,k):
        for i in range(2,k):
            if k%i ==0:
                return False
        return True
    def __iter__(self):
        for k in range(self.start,self.end+1):
            if self.isPrimeNumber(k):
                yield k

# for x in PrimeNumber(1,100):
#     print(x)
A =  PrimeNumber(1,100)
print(A.next)
