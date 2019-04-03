# -*- coding:utf-8 -*-
'''
筛选所需内容，字典数组
'''

#随机生成十个[-10 10]的随机数
from random import randint
data = [randint(-10,10) for _ in range(10)]
# print(data)
# 8, 3, -4, 6, -5, -3, -10, -9, -3, -7]
#比较 filter函数 和 列表解析
filter(lambda x: x>=0, data)
[x for x in data if x>=0]
#filter 比列表解析更耗时

#字典筛选
#创建20个分数在60-100之间的字典
d = {x:randint(60,100) for x in range(1,21)}
# print(d)
# {1: 71, 2: 76, 3: 86, 4: 71, 5: 77,
# 6: 98, 7: 92, 8: 71, 9: 74, 10: 68,
# 11: 95, 12: 90, 13: 68, 14: 91, 15: 79,
# 16: 97, 17: 71, 18: 71, 19: 96, 20: 79}
print({k:v for k,v in d.items() if v>90})
# {1: 99, 6: 91}
''' python2  在Python2.x中，items( )用于 返回一个字典的拷贝列表【Returns a copy of the list of all items (key/value pairs) in D】，占额外的内存。
iteritems() 用于返回本身字典列表操作后的迭代【Returns an iterator on all items(key/value pairs) in D】，不占用额外的内存。
>>> d={1:'one',2:'two',3:'three'}
>>> type(d.items())
<type 'list'>
>>> type(d.iteritems())
<type 'dictionary-itemiterator'>
>>> type(d.viewitems())
<type 'dict_items'>
'''
"""
Python 3.x 里面，iteritems() 和 viewitems() 这两个方法都已经废除了，
而 items() 得到的结果是和 2.x 里面 viewitems() 一致的。
在3.x 里 用 items()替换iteritems() ，可以用于 for 来循环遍历。
"""

# 集合解析
#set集合后，整数从小到大+负数从小到大
s = (set(data))
{x for x in s if x%3==0}
# {0, -3, 6, -9}


