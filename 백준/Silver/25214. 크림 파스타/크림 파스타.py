n = int(input())

ans = [0]
mn = float('inf')
for num in map(int, input().split()):
    mn = min(mn, num)
    ans.append(max(ans[-1], num-mn))

print(' '.join(map(str, ans[1:])))