def tell_story(person):
    print('小小少年', person, sep='')


tell_story('小伙子')

tell_story(person='小伙子2')


def add(a, b):
    """
    :param a: 1
    :param b: 2
    :return: 3
    """
    return a + b


print(add(1, 3))
help(add)


# 可变参数
# *args 可变参数
# **kwargs 关键字参数
def add2(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


# add2(1, 2, 4, 4, 5, 6, 2, 7, 3)
add2(1, 2, 4, 4, 5, 6, 2, 7, 3, c=1)

# 匿名函数
mul = lambda a, b: a + b
print(mul(1, 2))
