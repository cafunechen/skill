# # 将小字符串拼接为大字符串
s1 = ['222','333']
# s1+s2
'''
本质上是重载
'''
s = ''
for p in s1:
    s +=p
# 每一次都需要拷贝一次s，然后被释放，需要大量的空间
'''
str.join 方法
不会有临时变量的浪费
'''
print(';'.join(['abc','123','xyz']))
l = ['abc',123,45,'xyaz']
print(''.join([str(x) for x in l]))
# l列表解析会生成列表，也会有额外开销
print(''.join(str(x) for x in l))
# 生成器，不会有额外的开销
