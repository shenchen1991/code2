class Student(object):
    # 这个属性直接定义在类中，用来规定该类可以存着的属性
    __slots__ = ('name', 'age', 'height', 'city')

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __repr__(self):
        return 'test repr'

    # 优先走str函数
    def __str__(self):
        return 'test str'

    def __del__(self):
        print('销毁思密达')

    def run(self):
        print(self.name, '跑步')

    def eat(self):
        print('吃吃吃')


s1 = Student('小明', 10, 1.89)
# s2 = Student('小美丽', 17, 1.88)
print(s1)

# s1.run()
# s2.eat()

s1.city = '上海'
# print(s1.city)
