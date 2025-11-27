import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    a, b, c = sorted(map(int, input().split()))
    res = "YES" if c*c == a*a + b*b else "NO"
    print(f"Case #{i}: {res}")