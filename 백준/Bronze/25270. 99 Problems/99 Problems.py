n = int(input())

low = (n // 100) * 100 - 1
if low < 0:
    print(99)
    exit(0)
high = low + 100

print(low if 2*n < low+high else high)