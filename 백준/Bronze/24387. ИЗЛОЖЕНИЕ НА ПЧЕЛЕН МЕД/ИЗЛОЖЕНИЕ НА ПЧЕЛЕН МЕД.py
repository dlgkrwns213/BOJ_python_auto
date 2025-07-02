a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))

print(sum(map(lambda idx: a[idx] * b[idx], range(3))))