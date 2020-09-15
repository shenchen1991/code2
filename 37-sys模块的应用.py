import sys

s_in = sys.stdin

while True:
    content = s_in.readline().rstrip('\n')
    if content == 'exitc':
        break
    print(content)
