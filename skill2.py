# -*- coding:utf-8 -*-
'''
如何为元祖中的每个元素命名,提高程序可行性
'''
student = ('Jim', '16',"male",'jim@gmail.com')
student[1] ==16
'''
# python 类似的枚举类型
'''
Name =0
Age = 1
Sex = 2
Email = 3
Name ,Age,Sex ,Email = range(3)
'''

from collections import namedtuple
#创建类型 namedtuple('Student',['Name' ,'Age','Sex' ,'Email'])
Student = namedtuple('Student',['Name' ,'Age','Sex' ,'Email'])
s = Student('Jim', '16',"male",'jim@gmail.com')
# Student(Name='Jim', Age='16', Sex='male', Email='jim@gmail.com')
s2 =  Student('Jim', '16',"male",'jim@gmail.com')
s2.Name
# Jim
isinstance(s,tuple)
# Ture
