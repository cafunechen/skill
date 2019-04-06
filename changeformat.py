'''将年月日替换为别的格式 yyyy-mm-dd  mm/dd/yyyy'''
# log  = open('/var/log/dpkg.log').read()
log = '2016-05-30'
import  re
print(re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log))
# 三组 四个数字，2个数字
# r'\2(第二组）/\3(第3组）/\1(第1组）
print(re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',log))
# 注意是大P
