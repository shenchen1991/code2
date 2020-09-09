# 元组 不可修改
nums = (1, 2, 3, 4, 5)
print(nums[1])
print(nums.index(5))
print(nums.count(7))

ages = (10,)
print(type(ages))

print(tuple('10'))

names = ['a', 'b', 'c']
print(tuple(names))

print(list(nums))

# 字典
person = {
    'name': 'shenchen',
    'age': 18
}
print(person)
print(person['age'])
x = 'age'
print(person[x])
print(person.get('gender', 'False'))

person['name'] = 'lisi'
person['gender'] = 'M'

print(person)

# x = person.pop('name')
# print(x)
#
# result = person.popitem()
# print(result)

for x in person:
    print(x, '=', person[x])

print(person.keys())
for key in person.keys():
    print(key)

# 字典推导式
dict = {v: k for k, v in person.items()}
print(dict)

# 集合 无序
x = {'a', 18, 'a'}
print(x)

print(x.add('a'))
print(x)

# x.pop()
# print(x)

x.remove('a')
print(x)

y = {'a', 'g'}
print(x.union(y))

x.update(['m', 'n'])
print(x)

x.clear()
print(x)
