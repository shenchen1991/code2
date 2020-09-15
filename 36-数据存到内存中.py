from io import StringIO, BytesIO

s_io = StringIO()
print('hello', file=s_io)
print('hello', file=s_io)
print('hello', file=s_io)
print('hello', file=s_io)

print(s_io.getvalue())

b_io = BytesIO()
b_io.write('你好'.encode('utf-8'))
print(b_io.getvalue().decode('utf-8'))
