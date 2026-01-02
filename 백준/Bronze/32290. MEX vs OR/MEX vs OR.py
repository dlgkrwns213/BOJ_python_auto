l, r, x = map(int, input().split())

numbers = set()
for i in range(l, r+1):
    numbers.add(i | x)

for i in range(10000):
    if i not in numbers:
        print(i)
        break