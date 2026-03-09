x = int(input())
numbers = [2025, 3025, 9801]

for y in numbers:
    if y >= x + 1:
        print(y)
        exit(0)

print(-1)