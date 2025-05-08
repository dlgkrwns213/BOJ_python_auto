# https://www.acmicpc.net/problem/17840
q, m = map(int, input().split())

a, b = 1, 1
numbers = [1, 1]
while True:
    a, b = b, (a + b) % m
    if (a, b) == (1, 1):
        numbers.pop()
        break

    div = 1
    n = b
    while n // div >= 10:
        div *= 10

    n = b
    while div > 0:
        numbers.append(n//div)
        n %= div
        div //= 10

size = len(numbers)
print('\n'.join(map(lambda x: str(numbers[(x-1) % size]), (int(input()) for _ in range(q)))))