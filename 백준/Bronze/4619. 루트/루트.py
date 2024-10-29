import sys
input = sys.stdin.readline

ans = []
while True:
    b, n = map(int, input().split())
    if not b:
        break

    a, mn = 0, b
    while True:
        gap = abs(pow(a+1, n) - b)
        if gap > mn:
            break

        mn = gap
        a += 1

    ans.append(a)

print('\n'.join(map(str, ans)))