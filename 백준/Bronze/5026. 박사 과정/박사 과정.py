import sys
input = sys.stdin.readline

for _ in range(int(input())):
    ipt = input().rstrip()
    print(sum(map(int, ipt.split('+'))) if '+' in ipt else 'skipped')