# -*- coding:utf-8 -*-
'''
如何统计序列中元素出现的频度
'''
from random import randint
from collections import Counter
import re
'''常规想法，排序找最高'''
data = [randint(0,20) for _ in range(30)]
# [10, 5, 1, 1, 19, 0, 9, 13, 17, 20, 0, 12, 13, 20, 7, 14, 10, 13, 6, 3, 15, 4, 8, 13, 11, 8, 11, 11, 0, 18]
c = dict.fromkeys(data,0)
'''以data的值为key，构建字典，值为零'''
# {10: 0, 5: 0, 1: 0, 19: 0, 0: 0, 9: 0, 13: 0, 17: 0, 20: 0, 12: 0, 7: 0, 14: 0, 6: 0, 3: 0, 15: 0, 4: 0, 8: 0, 11: 0, 18: 0}
for x in data:
    c[x]+=1

'''更简洁的方法：collections 下的Counter函数'''
c2 = Counter(data)
# Counter({15: 4, 7: 3, 17: 3, 19: 3, 20: 2, 4: 2, 3: 2, 16: 2, 5: 2, 8: 1, 6: 1, 18: 1, 14: 1, 12: 1, 9: 1, 2: 1})
c2.most_common(3)

'''直接计算出现了多少次
注意形式，与Counter内容不一样，这里是数组
[(15, 4), (7, 3), (17, 3)]
'''


'''
文件的操作
'''
txt = open('skill3.txt').read()
# 用正则表达式进行分割
# \W非字母、非数字、非汉字、非_
c3 = Counter(re.split('\W+',txt))
c3.most_common(10)
'''
[('the', 21), ('and', 18), ('of', 12), ('constraint', 10), ('on', 10), 
('for', 8), ('with', 7), ('handling', 7), ('The', 7), ('are', 7)]
'''
