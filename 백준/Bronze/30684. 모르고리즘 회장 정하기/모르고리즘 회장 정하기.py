n = int(input())
print(sorted([x for x in (input() for _ in range(n)) if len(x) == 3])[0])