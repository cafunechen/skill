l =[1,2,3,4,5]
l.reverse()
print(l)
# [5, 4, 3, 2, 1]
print(l[::-1])
# [5, 4, 3, 2, 1]
# 这两种方法都会重新构建一个数组，浪费内存空间
print(reversed(l))
# 反向迭代器

# <list_reverseiterator object at 0x0000028574547048>
print(iter(l))
# 正向迭代器,等价于l.__iter__
# <list_iterator object at 0x000002857460AA90>
for x in reversed(l):
    print(x,end=' ')


class FLoatRang:
    def __init__(self,start,end,step =0.1):
        self.start = start
        self.end = end
        self.step = step
    def __iter__(self):
        t = self.start
        while t<=self.end:
            yield  t
            t+= self.step
    def __reversed__(self):
        t = self.end
        while t<=self.start:
            yield  t
            t-= self.step
for i in reversed(FLoatRang(1.0,4.0,0.5)):
    print(i)
