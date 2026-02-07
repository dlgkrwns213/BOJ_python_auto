answer = []
for _ in range(int(input())):
    a, b = map(float, input().split())
    answer.append(f"{abs(a-b):.1f}")
print('\n'.join(map(str, answer)))