def can_play(clock):
    def handle_action(fn):
        def do_action(name, game):
            if clock < 21:
                fn(name, game)
            else:
                print('晚了')

        return do_action

    return handle_action


@can_play(1)
def play_game(name, age):
    print(name, age)


play_game('张三', 2)

user_permission = 9

DEL_PERMISSION = 8
READ_PERMISSION = 4
WRITE_PERMISSION = 2
EXE_PERMISSION = 1


def check_permission(x, y):
    def handle_action(fn):
        def do_action():
            if x & y != 0:
                fn()
            else:
                print('没权限')

        return do_action

    return handle_action


@check_permission(user_permission, WRITE_PERMISSION)
def write():
    print('write')


@check_permission(user_permission, READ_PERMISSION)
def read():
    print('read')


@check_permission(user_permission, EXE_PERMISSION)
def exe():
    print('exe')


@check_permission(user_permission, DEL_PERMISSION)
def delete():
    print('delete')


write()
read()
exe()
delete()
