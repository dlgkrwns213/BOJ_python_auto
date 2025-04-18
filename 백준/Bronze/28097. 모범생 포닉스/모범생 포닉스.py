n = int(input())
print(*divmod(sum(map(int, input().split()))+8*(n-1), 24))