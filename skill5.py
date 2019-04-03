# -*- coding:utf-8 -*-
'''
如何快速找到多个字典中的公共建（key）
'''

"""
例子：每场比赛都进球的球员
"""
from functools import reduce
from random import randint,sample
sample('abcdefg',3)
# ['c','d','b']
sample('abcdefg',randint(3,6))

s1 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
# {'c': 1, 'f': 3, 'd': 1, 'e': 1, 'g': 4}
s2 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s3 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}

'''一种方法'''
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)

'''集合'''
# s1.viewkeys()
# dict_keys(['a','b','e','f'])
s1.keys() & s2.keys() & s3.keys()
# {'e', 'a'}

'''map'''
# map(dict.keys,[s1,s2,s3])
reduce(lambda a,b: a & b,map(dict.keys,[s1,s2,s3]))
# {'a', 'b'}
