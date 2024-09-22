# https://www.acmicpc.net/problem/5670
import sys
from collections import defaultdict
input = sys.stdin.readline
trie = lambda: defaultdict(trie)
END = '$'


def insert(word):
    node = root
    for char in word:
        node = node[char]
    node[END] = True


def counting(word):
    node = root
    cnt = 1

    for char in word[:-1]:
        node = node[char]
        if len(node) > 1 or END in node:
            cnt += 1

    return cnt


ans = []
while True:
    try:
        n = int(input())
    except (ValueError, EOFError):
        break

    words = [input().rstrip() for _ in range(n)]
    root = trie()
    for word in words:
        insert(word)

    total = 0
    for word in words:
        total += counting(word)
    ans.append(f'{total/n:.2f}')

print('\n'.join(ans))