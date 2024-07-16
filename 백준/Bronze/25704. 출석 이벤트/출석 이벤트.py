n = int(input())
p = int(input())

ans = p
if n >= 20:
    ans = min(p-2000, 3*p//4)
elif n >= 15:
    ans = min(9*p//10, p-2000)
elif n >= 10:
    ans = min(p-500, 9*p//10)
elif n >= 5:
    ans = p-500

print(max(0, ans))