values = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

n, m = map(int, input().split())
a, b = input().split()

merged = ''.join(''.join(pair) for pair in zip(a, b)) + (b[n:] if n < m else a[m:])

make = list(map(lambda x: values[ord(x)-ord('A')], merged))
while len(make) > 2:
    make = [(make[i]+make[i+1]) % 10 for i in range(len(make)-1)]

print(f'{int("".join(map(str, make)))}%')