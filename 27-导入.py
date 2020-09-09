import calendar
import hashlib
import hmac
import random
import time
import uuid
from random import randint
from math import *
import datetime as date
import os
import sys
import math
import datetime

print(date.MAXYEAR)
print(os.name)
print(os.sep)

print(sys.path)

# sys.stdin
# sys.stdout
# sys.stderr

print('-----------------math---------------------------')
print(math.factorial(6))
print(math.floor(12.98))
print(math.ceil(12.01))
print(math.pow(2, 3))  # 幂运算

# round() 内置函数，实现四舍五入

print(random.randint(2, 5))
# [0,1)随机数
print(random.random())
# [2,3)随机数
print(random.randrange(2, 3))

print(random.choice(['张三', '历史', '韩国']))

print('-----------------datetime---------------------------')
print(datetime.datetime.now())
print(datetime.date(2020, 1, 2))
print(datetime.time(2, 1, 2))
print(date.datetime.now() + datetime.timedelta(3))  # 计算三天以后的时间

print('-----------------calendar---------------------------')
print(calendar.calendar(2020))

print('-----------------hashlib 和 hmac---------------------------')
# 加密
# hashlib支持 md5 和sha 加密 单向加密
x = hashlib.md5()
x.update('abc'.encode('utf-8'))
print(x.hexdigest())
print(hashlib.md5('123'.encode()).hexdigest())

# 键值对单向加密
print(hmac.new('key'.encode(), '你好'.encode()).hexdigest())

print('-----------------uuid---------------------------')

print(uuid.uuid1())
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'zs'))
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'zs'))

print(uuid.uuid4())