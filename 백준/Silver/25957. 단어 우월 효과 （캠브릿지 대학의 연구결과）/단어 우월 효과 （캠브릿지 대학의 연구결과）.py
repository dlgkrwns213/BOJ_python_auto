import sys
input = sys.stdin.readline
hashed = lambda s: s[0] + s[-1] + ''.join(sorted(s))

words = dict()
for _ in range(int(input())):
    ipt = input().rstrip()
    words[hashed(ipt)] = ipt

input()
print(' '.join(map(lambda word: words[hashed(word)], input().split())))