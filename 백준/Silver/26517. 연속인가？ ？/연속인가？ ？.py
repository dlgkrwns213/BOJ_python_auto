k = int(input())
a, b, c, d = map(int, input().split())

left = a * k + b
right = c * k + d

print(f'Yes\n{left}' if left == right else 'No')