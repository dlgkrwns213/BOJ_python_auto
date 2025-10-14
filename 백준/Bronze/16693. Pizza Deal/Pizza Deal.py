from math import pi

a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())

sr = a1 / p1
wr = pi * r1 * r1 / p2

print('Whole pizza' if wr > sr else 'Slice of pizza')