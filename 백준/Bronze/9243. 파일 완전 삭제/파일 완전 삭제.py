n = int(input())
a, b = input(), input()
if n & 1:
    a = ''.join(map(lambda x: '1' if x == '0' else '0', a))
print(f'Deletion {"succeeded" if all(a[i] == b[i] for i in range(len(a))) else "failed"}')