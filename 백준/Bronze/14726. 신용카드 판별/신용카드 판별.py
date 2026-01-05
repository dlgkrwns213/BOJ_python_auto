import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    number = 0
    for i, x in enumerate(map(int, input().rstrip()[::-1])):
        if i % 2:
            x *= 2
            x = x // 10 + x % 10

        number += x

    ans.append('F' if number % 10 else 'T')

print('\n'.join(ans))