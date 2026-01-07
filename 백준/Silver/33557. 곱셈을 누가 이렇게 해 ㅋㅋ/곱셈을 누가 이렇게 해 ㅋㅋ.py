import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    a, b = input().split()
    if len(a) < len(b):
        a, b = b, a
        
    x = str(int(a) * int(b))
    y = []
    a, b = a[::-1], b[::-1]
    for i in range(len(b)):
        y.append(int(a[i]) * int(b[i]))
    for i in range(len(b), len(a)):
        y.append(a[i])

    ans.append('1' if ''.join(map(str, y[::-1])) == x else '0')

print('\n'.join(ans))
