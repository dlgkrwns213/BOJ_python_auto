input()

ans = 1
for num in list(map(int, input().split()))[::-1]:
    ans = ((ans + num - 1) // num) * num

print(ans)
