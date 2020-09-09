import json

# a = 'print(input("输入一波"))'
# eval(a)

n = '["hello","good"]'
s = json.loads(n)
print(s)
print(json.dumps(['test', False]))
