n, l, h = map(int, input().split())
scores = sorted(map(int, input().split()))[l:n-h]

print(sum(scores) / len(scores))