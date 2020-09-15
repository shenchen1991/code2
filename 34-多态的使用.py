class Dog(object):

    def work(self):
        print('working')


class PoliceDog(Dog):
    def work(self):
        print('警犬working')


class Person(object):
    def __init__(self, name):
        self.name = name
        self.dog = None

    def work_with_dog(self):
        if self.dog is not None and isinstance(self.dog, Dog):
            self.dog.work()


p = Person('wang')
pd = PoliceDog()
p.dog = pd
p.work_with_dog()
