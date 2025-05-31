import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.weight = 0
        self.children = []


n = int(input())
Nodes = []
for i in range(n+1):
    Nodes.append(Node(i))

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    Nodes[child].weight = weight
    Nodes[parent].children.append(Nodes[child])


def find(node):
    print(node.data, node.weight, node.children)
    for children in node.children:
        find(children)


def get_weight(node):
    if not node.children:
        return 0
    else:
        child_num = len(node.children)
        weights = [0] * child_num
        for i, child in enumerate(node.children):
            weights[i] = child.weight + get_weight(child)

        weight_list.append(weights)
        # print(node.data, ':', weights)

        return max(weights)


# find(Nodes[1])
weight_list = [[0]]
get_weight(Nodes[1])
# print(weight_list)

M = 0
for w in weight_list:
    if len(w) == 1:
        M = max(M, w[0])
    else:
        one = max(w)
        w.remove(one)
        two = max(w)
        M = max(M, one + two)
print(M)