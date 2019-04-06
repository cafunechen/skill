# 如何在一个for语句中迭代多个可迭代对象
from random import  randint
from itertools import chain
chinese = [randint(60,100) for _ in  range(40)]
math = [randint(60,100) for _ in  range(40)]
english = [randint(60,100) for _ in  range(40)]
# 使用zip，可以将多个可迭代对象合并起来
# 并行
total = []
for c,m,e in zip(chinese,math,english):
    total.append(c+m+e)
# 使用itertools.chain 连接多个可迭代对象
# 串行
e1 = [randint(60,100) for _ in  range(40)]
e2 = [randint(60,100) for _ in  range(42)]
e3 = [randint(60,100) for _ in  range(39)]
e4 = [randint(60,100) for _ in  range(41)]
count =0
for s in chain(e1,e2,e3,e4):
    if s>90:
        count+=1

print(count)
