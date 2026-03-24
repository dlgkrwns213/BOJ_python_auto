from itertools import permutations


def is_possible(pmt):
    pmt_str = [str(x) for x in pmt]

    total = 0
    for word in words[:-1]:
        make = ''.join(pmt_str[indexes[x]] for x in word)
        if make[0] == '0':
            return False
        total += int(make)

    last = ''.join(pmt_str[indexes[x]] for x in words[-1])
    if last[0] == '0':
        return False

    return total == int(last)


n = int(input())
words = [input() for _ in range(n)]

uses = set()
for word in words:
    uses |= set(word)
uses = list(uses)
indexes = {v: i for i, v in enumerate(uses)}

count = 0
for pmt in permutations(list(range(10)), len(uses)):
    count += is_possible(pmt)
print(count)