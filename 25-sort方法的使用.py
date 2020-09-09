from functools import reduce

num1 = [6, 4, 5, 71, 2]
num1.sort()
print(num1)
num2 = [6, 4, 5, 71, 2]
print(sorted(num2))


def foo(ele):
    pass


# 字典排序
students = [{'name': 'zhangsan', 'age': 18},
            {'name': 'zhangsan2', 'age': 8},
            {'name': 'zhangsan3', 'age': 138},
            {'name': 'zhangsan4', 'age': 128},
            ]

students.sort(key=lambda ele: ele['age'], reverse=True)
print(students)

# filter
ages = [33, 4, 55, 67, 1, 3, 5]
# print(filter(lambda ele: ele > 18, ages))
# for age in filter(lambda ele: ele > 19, ages):
#     print(age)

# map
map(lambda ele: ele + 2, ages)
for age in map(lambda ele: ele + 2, ages):
    print(age)

# reduce
ages = [33, 4, 55, 67, 1, 3, 5]
print(reduce(lambda ele1, ele2: ele1 + ele2, ages))

students = [{'name': 'zhangsan3', 'age': 138},
            {'name': 'zhangsan4', 'age': 128},
            {'name': 'zhangsan', 'age': 18},
            {'name': 'zhangsan2', 'age': 8}]

print('reduce(lambda ele1, ele2: ele1 + ele2, ages)')


def bar(x, y):
    return x + y['age']


print(reduce(bar, students, 0))
