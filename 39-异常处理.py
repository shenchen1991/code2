def div(a, b):
    return a / b


try:
    x = div(4, 0)
except Exception as e:
    print('出错')
else:
    print(x)
finally:
    print('finally')
