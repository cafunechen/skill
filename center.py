# 字符串对齐
# 1、str.ljust()
s = 'abc'
s.ljust(20)
# 'abc                 '
s.ljust(20,'-')
# 'abc-----------------'
s.rjust(20)
# '                 abc'
s.center(20)
# '       abc          '
# 2、format
format(s,'<20')
# 'abc                 '
format(s,'>20')
# '                 abc'
format(s,'^20')
# '       abc          '
d = {'a':20200,'ddd':33,'ddddd':1}
w = max(map(len,d.keys()))
# 取最大长度
for k in d:
    print(k.ljust(w), ':' ,d[k])
'''
a     : 20200
ddd   : 33
ddddd : 1
'''
