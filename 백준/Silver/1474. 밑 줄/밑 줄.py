import sys
input = sys.stdin.readline


n, m = map(int, input().split())
words = [input().rstrip() for _ in range(n)]

use = m - sum(map(len, words))
one, plus = divmod(use, n-1)

ans = [words[0]]
for word in words[1:]:
    if (word[0].islower() and plus) or n-2 < plus:
        ans.append('_'*(one+1))
        plus -= 1
    else:
        ans.append('_'*one)
    ans.append(word)
    n -= 1

print(''.join(ans))