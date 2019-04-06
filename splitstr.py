# 如何拆分多个字符串
s = 'ab;cd/efg/jf.kld/dkjlafd\;ddd --'
s.split()
# 当有多个分割符
'''
res = s.split(';')
map(lambda x:x.split('/'),res)
这样会增加维数[[]]
'''
'''
为了解决上述问题
可以用
map(lamda x:t.extend(x.split('/'),res)
拓展开
map结果为空[none,none,none]，
因为结果都扩展到t里面
t = ['ab','cd'...]
依次类推
因此可以写一个函数
'''
def mySplit(s,ds):
    res = [s]
    for d in ds:
        t = []
        map(lamda x:t.extend(x.split(d),res)
        res =  t
    return [x for x in res if x]
    # 过滤连续字符串所留下的空字符串
import re
'''正则表达式'''
re.split(r'[,;\t|+',s)
