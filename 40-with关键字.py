# try:
#     file = open('xxx.txt', 'rb')
# except FileNotFoundError:
#     print('文件不存在')
# else:
#     try:
#         file.read()
#     finally:
#         file.close()

# with关键字会帮助自动关闭文件流 ，上下文管理器
# 需要重写__enter__ 和__exit__关键字
try:
    with open('xxx.txt', 'rb') as file:
        file.read()
except FileNotFoundError:
    print('文件不存在')


class Demo(object):

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def create_d():
    x = Demo()
    return x


# 执行流程create_d().__enter__
with create_d() as d:
    print(d)