# 一个模块本质商就是一个py文件
import demo
from demo import *

print(demo.a)
print(demo.m)

demo._age

import datetime