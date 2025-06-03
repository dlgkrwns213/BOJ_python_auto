n = int(input())
locations = [list(map(int, input().split())) for _ in range(n)]

print(*min(locations, key=lambda location: location[1]))