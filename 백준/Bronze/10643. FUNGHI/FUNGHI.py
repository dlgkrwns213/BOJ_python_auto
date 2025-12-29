a = [int(input()) for _ in range(8)] * 2
print(max(sum(a[i:i+4]) for i in range(8)))