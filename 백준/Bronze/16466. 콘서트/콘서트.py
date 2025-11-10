n = int(input())
numbers = set(map(int, input().split()))
for i in range(1, n+2):
    if i not in numbers:
        print(i)
        break