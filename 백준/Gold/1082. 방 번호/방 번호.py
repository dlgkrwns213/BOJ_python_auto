def find(now, rest):
    ret = [i for i, v in enumerate(prices) if v == now][-1]
    for i in range(ret + 1, n):
        if 0 < prices[i] - now <= rest:
            ret = i

    return ret, rest - prices[ret] + now


n = int(input())
prices = list(map(int, input().split()))
m = int(input())

if n == 1:
    print(0)
    exit(0)

a = min(prices[1:])
m -= a
if m < 0:
    print(0)
    exit(0)

x, rest = divmod(m, min(prices))  # 자릿수 : x+1
first, rest = find(a, rest)
ans = [first]
for _ in range(x):
    num, rest = find(min(prices), rest)
    ans.append(num)

print(''.join(map(str, ans)))