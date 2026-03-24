from itertools import permutations


def is_possible(pmt):
    total = 0
    for c, w in weight.items():
        total += pmt[indexes[c]] * w
    return total == 0


n = int(input())
words = [input() for _ in range(n)]

uses = set()
for word in words:
    uses |= set(word)
uses = list(uses)
indexes = {v: i for i, v in enumerate(uses)}

leading = set(word[0] for word in words)
weight = {c: 0 for c in uses}

for word in words[:-1]:
    digit = 1
    for c in reversed(word):
        weight[c] += digit
        digit *= 10

digit = 1
for c in reversed(words[-1]):
    weight[c] -= digit
    digit *= 10

count = 0
for pmt in permutations(list(range(10)), len(uses)):
    valid = True
    for c in leading:
        if pmt[indexes[c]] == 0:
            valid = False
            break
    if not valid:
        continue
    count += is_possible(pmt)

print(count)