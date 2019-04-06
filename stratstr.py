# 如何判断字符串a是否以字符串b开头或结尾
import  os, stat
# os 系统调用
# stat 文件状态
# os.listdir('.')
# 当前目录下的所有文件
s = 'g.sh'
print(s.endswith(('.sh','.py')))
# 只能是元组不能是列表
[for name in os.listdir('.') if name.endswith(('.sh','.py'))]
os.stat('e.py')
# 文件权限
os.stat('e.py').st_mode
# 返回一个进制数
oct(os.stat('e.py').st_mode)
# 转换成十进制
stat.S_IXUSR
#  i x usr
os.chmod('e.py', os.stat('e.py').st_mode | stat.S_IXUSR)
# 修改该文件的用户权限
