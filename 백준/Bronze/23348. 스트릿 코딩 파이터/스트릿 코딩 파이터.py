scores = list(map(int, input().split()))
mx = 0
for _ in range(int(input())):
    x = sum([list(map(int, input().split())) for _ in range(3)], [])
    total = sum(map(lambda idx: scores[idx%3] * x[idx], range(9)))

    mx = max(mx, total)
print(mx)