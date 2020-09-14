__all__ = ['a']
a = 'rest'
m = 'restm'

# 以一个下划线开始的变量，建议别的模块不要导入
_age = 10

# 被导入时不执行
if __name__ == '__main__':
    print('test')
