
# __iter__
# __getitem__
'''
for i in list的工作过程：
 先对list生成iter
 然后 list.next
 直到stop
'''
'''
迭代器对象Iterator和可迭代对象Iterable是不一样的
x.next,x.__iter__

'''
import requests
from collections.abc import Iterable,Iterator

#[u"北京",u"上海",u"广州'，u'长春']
class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city  = self.cities[self.index]
        self.index+= 1
        return self.getweather(city)

    def getweather(self,city):
        r = requests.get(u"http://wthrcdn.etouch.cn/weather_mini?city=" +city)
        data = r.json()['data']['forecast'][0]
        return ("%s:%s,%s"%(city,data['low'],data['high']))

class WeatherIterable(Iterable):
    def __init__(self,cities):
        print(cities)
        self.cities = cities
    def __iter__(self):
        return WeatherIterator(self.cities)
# print(gerweather(u"北京"))

for x in WeatherIterable([u"北京",u'上海',u'广州',u'长春']):
    print(x)
