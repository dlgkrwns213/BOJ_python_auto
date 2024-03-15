n = int(input())
A = list(map(int, input().split()))

ans = [b for i, b in enumerate(map(int, input().split())) if not A[i]]
ans.reverse()

m = int(input())
ans += list(map(int, input().split()))

print(' '.join(map(str, ans[:m])))