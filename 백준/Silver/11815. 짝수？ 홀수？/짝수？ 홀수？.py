from math import sqrt

input()
print(' '.join(map(lambda x: '1' if int(sqrt(x))**2 == x else '0', map(int, input().split()))))