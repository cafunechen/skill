'''
用迭代器做切片操作
Python中的文本文件是可迭代对象!!!
'''
from itertools import islice
f = open('skill3.txt')
f.read(4)
# 上述方法不能迭代
# f.seek(0)
#一种方法，但是readline读取所有，内存较大
# lines  = f.readlines()
# lines[100:300]
#
# for line in islice(f,100,300):
#     print(line)
