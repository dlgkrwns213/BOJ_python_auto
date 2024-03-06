n = int(input())
print(sum(map(lambda x: min(n, int(x)), input().split())))