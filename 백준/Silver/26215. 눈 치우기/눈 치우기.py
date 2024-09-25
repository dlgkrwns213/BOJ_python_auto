n = int(input())
snows = list(map(int, input().split()))
total, mx = sum(snows), max(snows)
ans = total+1 >> 1 if total >= 2*mx else mx
print(ans if ans <= 1440 else -1)