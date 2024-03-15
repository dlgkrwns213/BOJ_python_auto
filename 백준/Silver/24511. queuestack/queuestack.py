n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
m = int(input())

ans = []
for i in range(n-1, -1, -1):
    if not A[i]:
        ans.append(B[i])
ans += list(map(int, input().split()))

print(' '.join(map(str, ans[:m])))