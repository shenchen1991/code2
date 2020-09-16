nums = [i for i in range(10)]
print(nums)


def my_gen(n):
    i = 0
    while i < n:
        yield i
        i += 1


G = my_gen(10)
print(G)
for i in G:
    print(i)
