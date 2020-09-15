class Animal(object):
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.__money = 1000

    def sleep(self):
        print(self.name, '正在睡觉')

    def __test(self):
        print('Animal 私有方法')


class Dog(Animal):
    def bark(self):
        print(self.name, '正在叫')

    def __dotest(self):
        print('dog 私有方法')


class Student(Animal):
    def study(self):
        print(self.name, '正在学习')


class A(object):
    def foo(self):
        print('我收A方法的foo')


class B(object):
    def foo(self):
        print('我收B方法的foo')


class C(A, B):
    pass


dog = Dog('大黄', 19)
dog.bark()
dog._Animal__test()
dog._Dog__dotest()
print(dog._Animal__money)

c = C()
c.foo()