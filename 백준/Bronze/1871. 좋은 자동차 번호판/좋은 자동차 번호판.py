import sys
input = sys.stdin.readline

for _ in range(int(input())):
    front, back = input().split('-')

    fi = sum(map(lambda i: ((ord(front[i])-ord('A')) * (26 ** (2-i))), range(3)))
    print('nice' if abs(int(back)-fi) <= 100 else 'not nice')