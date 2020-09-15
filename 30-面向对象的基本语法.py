class Student(object):
    # 这个属性直接定义在类中，用来规定该类可以存着的属性
    # __slots__ = ('name', 'age', 'height', 'city')

    type = 'Student'

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.__money = 1000

    def __repr__(self):
        return 'test repr'

    # 优先走str函数
    def __str__(self):
        return self.name

    def __del__(self):
        print('销毁思密达')

    def __call__(self, *args, **kwargs):
        print('call 被调了')

    def __eq__(self, other):
        return self.name == other.name

    def run(self):
        print(self.name, '跑步')

    def eat(self):
        print('吃吃吃')

    @staticmethod
    def demo(x, y):
        return x + y

    @classmethod
    def test(cls):
        return cls.type


s1 = Student('小明', 10, 1.89)
s3 = Student('小明', 10, 1.89)
s2 = Student('小美丽', 17, 1.88)

print('s1 is s3', s1 is s3)

# 判断一个对象是否是由指定的类（或者父类）实例化的
print(isinstance(s1, (Student)))

print(issubclass(Student, object))

print('s1 == s3', s1 == s3)
print(s1)

s1()

# s1.run()
# s2.eat()

s1.city = '上海'
# print(s1.city)

print(s1.__dict__)

# 获取私有变量
print(s1._Student__money)

Student.eat(s1)
print(Student.demo(1, 2))

print(Student.test())
