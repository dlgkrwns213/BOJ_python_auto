n = int(input())
needs = list(map(int, input().split()))
t, p = map(int, input().split())

print(sum(map(lambda need: (need + t -1)//t, needs)))
print(*divmod(n, p))