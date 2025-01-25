import sys
input = sys.stdin.readline

n, l = map(int, input().split())

bef, time = 0, 0  # 이전 위치, 걸린 시간
for _ in range(n):
    d, r, g = map(int, input().split())

    # 이전 신호등부터 현재 신호등까지 이동시간
    time += d - bef
    bef = d

    # 현재 신호등에서 기다린 시간
    time += max(r - time % (r + g), 0)
time += l - bef

print(time)