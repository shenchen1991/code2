import random

names = ['A', 'B', 'C', 'D', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
rooms = [[], [], []]

for name in names:
    room = random.choice(rooms)
    room.append(name)

print(rooms)

for i, room in enumerate(rooms):
    print('房间%d总共%d个老师' % (i, len(room)))
    for name in room:
        print(name, end=' ')
    print()

# 列表推导式
nums = [i for i in range(10)]
print(nums)
for index in range(10):
    print(index)
print(range(10))

points = [(x, y) for x in range(2, 4) for y in range(4, 7)]
print(points)
