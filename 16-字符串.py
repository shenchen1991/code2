word = 'shenchen'

print(word[1])
# 包含start 不包含结尾
print(word[2:4])
print(word[2:])
print(word[:3])

# 每隔step-1个去一次
print(word[2:4:2])

# 倒序
print(word[::-1])

print(word[-7:-5])

print(len(word))

print(word.find('e'))
print(word.index('e'))
print(word.find('l'))
# print(word.index('l'))

# 纯字母
print('hel1lo'.isalpha())

# 纯数字
print('1a1'.isdigit())

# 纯数字字母
print('!!'.isalnum())

word = 'hello'
m = word.replace('l', 'x')
print(word)
print(m)

print('shenchen'.capitalize())

print('shenchen test.shenchen test'.capitalize())

print('shenchen'.upper())

print('shen chen'.title())

print('hello'.ljust(10))
print('hello'.ljust(10, '+'))
print('hello'.rjust(10, '+'))

print('hello'.center(11, '+'))

print('     hello  '.lstrip())
print('     hello  '.rstrip())
print('     hello  '.strip())

x = 'zhangan,lisi,wangwui';
list = x.split(',')
print(list)

names = ['zhangan', 'lisi', 'wangwui']
print('-'.join(names))
print('*'.join('test'))
print('-'.join(('yes', 'hello')))

name = '张三'
age = 18
print('大家好，我的名字是', name, '今年', age, sep='')
print('大家好，我的名字是%s,今年%s' % (name, age))

print('大家好，我的名字是%s,今年%03d' % (name, age))
print('大家好，我的名字是%s,今年%-5d' % (name, age))

print('大家好,我是{}，今年{}岁'.format('张三', 30))

print('大家好,我是{1}，今年{0}岁'.format(30, '张三'))
print('大家好,我是{name}，今年{age}岁'.format(age=30, name='张三'))

d = ['张三', 90]
print('大家好,我是{}，今年{}岁'.format(*d))

info = {'name': '张三', 'age': 19}
print('大家好,我是{name}，今年{age}岁'.format(**info))
