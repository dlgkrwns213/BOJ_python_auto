input()
numbers = list(map(int, input().split()))

indexs = {v: i for i, v in enumerate(sorted(set(numbers)))}
print(' '.join(map(lambda number: str(indexs[number]), numbers)))