def count(t):
    return str((0 < t % (a + b) <= a) + (0 < t % (c + d) <= c))


a, b, c, d = map(int, input().split())
print('\n'.join(map(count, map(int, input().split()))))