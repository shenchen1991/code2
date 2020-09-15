# mode
# r  只读模式

# file = open('xxx.txt', 'r', encoding='utf-8')
# file.write('sadasda')
# print(file.read())

# w 写入模式 文件存在会覆盖 不存在则创建
# file = open('xxx1.txt', 'w', encoding='utf-8')
# file.write('sadasda')

# b 二进制打开文件
# rb 二进制打开文件
import os

file = open('xxx.txt', 'rb')
# print(file.read())
print(file.readlines())

# file = open('xxx.txt', 'wb')
# file.write('奥术大师大qweqweq'.encode('utf-8'))

print(os.path.splitext('xxx.txt'))
