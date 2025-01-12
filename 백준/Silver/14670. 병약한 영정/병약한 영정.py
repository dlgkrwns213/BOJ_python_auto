import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
medicines = defaultdict(lambda: -1)
for _ in range(n):
    e, n = map(int, input().split())
    medicines[e] = n

ans = []
for _ in range(int(input())):
    eat = [medicines[symptom] for symptom in map(int, input().split()[1:])]
    ans.append(' '.join(map(str, eat)) if -1 not in eat else 'YOU DIED')

print('\n'.join(ans))