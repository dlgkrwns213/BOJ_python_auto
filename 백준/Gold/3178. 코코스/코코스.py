# https://www.acmicpc.net/problem/3178
import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
trie = lambda: defaultdict(trie)
END = '$'


def insert(root, word):
    node = root
    for char in word:
        node = node[char]
    node[END] = True


def counting(node):
    cnt = 1
    for nxt in node:
        if nxt != END:
            cnt += counting(node[nxt])
    return cnt


if __name__ == '__main__':
    front, back = trie(), trie()
    n, k = map(int, input().split())
    for _ in range(n):
        word = input().rstrip()
        insert(front, word[:k])
        insert(back, word[-1:k-1:-1])

    print(counting(front)+counting(back)-2)