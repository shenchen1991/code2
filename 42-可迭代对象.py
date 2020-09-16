import time
from collections.abc import Iterable


class Foo(object):
    def __next__(self):
        return 1


class Demo(object):
    def __init__(self, x):
        self.x = x
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.x:
            return 'text'
        else:
            raise StopIteration


d = Demo(1)
print(isinstance(d, Iterable))

for x in d:
    print(x)


class Fibonacci(object):
    def __init__(self, n):
        self.n = n
        self.num1 = self.num2 = 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index <= self.n:
            x = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return x
        else:
            raise StopIteration


f = Fibonacci(300)
for i in f:
    print(i)
