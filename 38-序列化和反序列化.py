import json
import pickle

file = open('names.txt', 'w', encoding='utf-8')

names = ['zhangsan', 'lisi', 'jack', 'tony']

# 序列化方法 dumps dump
# x = json.dumps(names)
# print(x)
# file.write(x)
# file.write(str(names))

json.dump(names, file)

file.close()

# 反序列化 loads load
x = '["zhangsan", "lisi", "jack", "tony"]'
p = json.loads(x)
print(p)

file1 = open('names.txt', 'r', encoding='utf-8')
y = json.load(file1)
print(y)
file1.close()

# pickle 序列化 dumps dump
b_names = pickle.dumps(names)
print(b_names)
file2 = open('names2.txt', 'wb')
file2.write(b_names)
file2.close()

# 反序列化 loads load
file3 = open('names2.txt', 'rb')
x = file3.read()
y = pickle.loads(x)
print(y)
file3.close()
