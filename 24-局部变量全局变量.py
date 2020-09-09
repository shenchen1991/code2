word = '全局'


def test():
    print(word)
    # global word
    # word = '局部'
    # print(word)
    # print(locals())
    # print(globals())


test()


def test2(person, city='南京'):
    print(person, city)


test2('test2', city='北京')
