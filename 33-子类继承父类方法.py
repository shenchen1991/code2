class Person(object):
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def sleep(self):
        print(self.name, '正在sleep')


class Student(Person):
    def __init__(self, name, age, score):
        # Person.__init__(self, name, age)
        super(Student, self).__init__(name, age)
        self.score = score

    def sleep(self):
        print(self.name, '课间睡觉')

    def study(self):
        print(self.name, '正在study')


s = Student('小明', 22, 33)
s.sleep()
