class Singleton:
    __instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return self.a + self.b


s1 = Singleton('hh', 'heheheheh')
s2 = Singleton('xx', 'xxxx')

print(s1 is s2)

print(s1)
print(s2)
