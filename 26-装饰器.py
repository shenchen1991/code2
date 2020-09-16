import time


def cal_time(fn):
    def inner(num):
        start = time.time()
        s = fn(num)
        end = time.time()
        print('耗时', end - start)
        return s

    return inner


@cal_time
def demo(num):
    x = 0
    for i in range(num):
        x += i
    print(x)
    return x


# print(demo(1000000))


def can_play(fn):
    def inner(x, y, **kwargs):
        clock = kwargs.get('clock', 23)
        if clock < 18:
            fn(x, y)
        else:
            print('sleep')
        pass

    return inner


@can_play
def play_game(name, age):
    print(name, age)


play_game('张三', 2)
