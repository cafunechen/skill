# -*- coding:utf-8 -*-
'''
如何实现用户历史记录
'''
from random import randint
from collections import deque
import pickle

# deque 队列
N = randint(0,100)
histrory = deque([],5)

def guess(k):
    if k == N:
        print('right')
        return True
    if k<N:
        print('%s is less than N'% k)
    else:
        print('%s id greater than N' % k)
    return False

while True:
    line = input('please input a number:')
    if line.isdigit():
        k = int(line)
        histrory.append(k)
        pickle.dump(histrory,open('skill6.txt','wb'))

        q2 = pickle.load(open('skill6.txt','rb'))
        if guess(k):
            break
    elif line =='history' or line =='h?':
        print(list(histrory))

# history保存在内存中
# 思考：如何保存到文件中




