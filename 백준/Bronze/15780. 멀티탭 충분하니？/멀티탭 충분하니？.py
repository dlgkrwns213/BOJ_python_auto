n, k = map(int, input().split())
possible = sum(map(lambda x: int(x)+1 >> 1, input().split()))

print('YES' if possible >= n else 'NO')