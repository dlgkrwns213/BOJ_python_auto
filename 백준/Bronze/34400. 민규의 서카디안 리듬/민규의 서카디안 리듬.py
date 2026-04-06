import sys
input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    answer.append(int(input()) % 25 < 17)
print('\n'.join(map(lambda x: ('OFFLINE', 'ONLINE')[x], answer)))