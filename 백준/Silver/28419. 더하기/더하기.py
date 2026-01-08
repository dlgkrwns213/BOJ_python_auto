n = int(input())
numbers = list(map(int, input().split()))

total = 0
for i, number in enumerate(numbers):
    if i % 2:
        total += number
    else:
        total -= number

print(max(total, -1) if n == 3 else abs(total))