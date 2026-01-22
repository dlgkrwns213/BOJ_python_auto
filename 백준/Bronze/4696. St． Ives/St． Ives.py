import sys
input = sys.stdin.readline

answer = []
while True:
    n = float(input())
    if not n:
        break

    answer.append(f'{sum(n**k for k in range(5)):.2f}')

print('\n'.join(answer))