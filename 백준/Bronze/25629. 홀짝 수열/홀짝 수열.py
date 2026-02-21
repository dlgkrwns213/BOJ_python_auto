input()

counts = [0, 0]
for num in map(int, input().split()):
    counts[num%2] += 1

a, b = counts
print(1 if b in (a, a+1) else 0)