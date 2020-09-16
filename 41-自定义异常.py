class LengthError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{}至{}之间'.format(self.x, self.y)


password = input('请输入密码')
max = 12
min = 6

if min <= len(password) <= max:
    print('ok')
else:
    raise LengthError(min, max)
