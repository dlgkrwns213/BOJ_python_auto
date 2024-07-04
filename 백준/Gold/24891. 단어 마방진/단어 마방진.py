from itertools import permutations


def checking(perm):
    uses = [words[i] for i in perm]
    for i in range(l):
        for j in range(i+1, l):
            if uses[i][j] != uses[j][i]:
                return False

    print('\n'.join(uses))
    return True


l, n = map(int, input().split())
words = [input() for _ in range(n)]
words.sort()

possible = False
for perm in permutations(range(n), l):
    if checking(perm):
        possible = True
        break

if not possible:
    print('NONE')