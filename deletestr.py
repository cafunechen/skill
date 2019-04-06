'''
strip()方法
'''
import  re
s = '       a  b      '
s.strip()
# 去掉两端的空白
# 'a   b'
s.lstrip()
# 去掉左端空白
# ‘a  b      ’
s.rstrip()
# s = '+++ssss===
s.strip('+=')
#ssss
'''
切片加拼接
'''
s = 'abs:123'
s[:3]+s[4:]
'''
replace,re,sub替换方法
'''
s = '\t123\tabs\t444'
s.replace('\t','')

s = '\t123\tabs\r444'
re.sub('\t\r','',s)

'''
translate
'''

s ='zxczxcabcacb'
str.maketrans('abcxyz','xyzabd')
print(s.translate(str.maketrans('abcxyz','xyzabd')))
# 第一个为None,不做任何映射
s,translate(None,'\r\t')


'''
去除音调
u= u'ni^  chi^...'
字母后面跟了一个数字
ni\v0301

'''
#
u.translate({dict.fromkeys([0x0301,0x0301])},None)
