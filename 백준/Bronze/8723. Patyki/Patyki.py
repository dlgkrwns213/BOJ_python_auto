a, b, c = sorted(map(int, input().split()))
if a == b == c:
    print(2)
elif a * a + b * b == c * c:
    print(1)
else:
    print(0)