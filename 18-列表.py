names = ['A', 'B', 'C', 'D', 'e', 'f']
names[2] = 'DD'
print(names[2])
print(names[3:5])

names2 = list(('a', 'b', 'c'))
print(names2)
names2.append('d')
names2.insert(2, 'G')
names2.extend(names2)
print(names2)

masters = ['h1', 'h2', 'h3', 'h4']
h4 = masters.pop()
print(masters)
print(h4)

masters.pop(2)
print(masters)

masters.remove('h1')
print(masters)

masters.clear()
print(masters)

masters2 = ['h1', 'h2', 'h3', 'h4', 'h4', 'h4']

del masters2[2]
print(masters2)
print('===')
print(masters2.index('h4'))
print(masters2.count('h4'))

print('h4' in masters2)
print('4' in masters2)

killers = ['k1', 'k2', 'k3', 'k4', 'k5']
for killer in killers:
    print(killer)

numbers = [2, 4, 7, 1, 0]
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)
print(sorted(numbers))



