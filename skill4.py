# -*- coding:utf-8 -*-
'''
根据字典中值得大小，对字典的项排序
'''
from random import randint

d = {x: randint(69,100) for x in 'xyzabc'}
# {'x': 86, 'y': 88, 'z': 83, 'a': 76, 'b': 70, 'c': 90}

sorted(d)
# ['a', 'b', 'c', 'x', 'y', 'z']

list(iter(d))
# ['x', 'y', 'z', 'a', 'b', 'c']

'''
zip函数+sort
'''
sorted(zip(d.values(),d.keys()))
# [(74, 'y'), (80, 'z'), (86, 'c'), (93, 'a'), (98, 'b'), (98, 'x')]

'''
用key 
'''
print(sorted(d.items(),key = lambda x:x[1]))
# [('a', 73), ('b', 73), ('x', 76), ('y', 76), ('c', 79), ('z', 82)]
