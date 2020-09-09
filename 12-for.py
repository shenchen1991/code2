# for i in range(1, 11):
#     print(i)

for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, '是质数')
