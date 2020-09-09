word = 'hello'
x = input('请输入：')

# for c in word:
#     if c == x:
#         print('存在')
#         break
# else:
#     print('不存在')

# if word.find(x) == -1:
#     print('不存在')
# else:
#     print('存在')


if x in word:
    print('存在')
else:
    print('不存在')