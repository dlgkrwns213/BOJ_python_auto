a, d, k = map(int, input().split())

n, r = divmod(k-a, d)
print('X' if r or n < 0 else n+1)