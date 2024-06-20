# https://www.acmicpc.net/problem/14570
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


class Node:
    def __init__(self, value):
        self.parent = 0
        self.child = []
        self.leaf_counts = []


def dfs(now):
    is_leaf = True
    for child in nodes[now].child:
        nodes[now].leaf_counts.append(dfs(child))
        is_leaf = False

    return sum(nodes[now].leaf_counts) + (1 if is_leaf else 0)


def give(now, rest):
    cc = len(nodes[now].child)
    if not cc:
        return now
    elif cc == 1:
        [child] = nodes[now].child
        return give(child, rest)

    left_child, right_child = nodes[now].child
    if rest & 1:
        return give(left_child, rest+1 >> 1)
    else:
        return give(right_child, rest >> 1)


n = int(input())
nodes: list[Node] = [Node(i) for i in range(n+1)]
for i in range(1, n+1):
    u, v = map(int, input().split())
    if u != -1:
        nodes[u].parent = i
        nodes[i].child.append(u)
    if v != -1:
        nodes[v].parent = i
        nodes[i].child.append(v)

dfs(1)
print(give(1, int(input())))