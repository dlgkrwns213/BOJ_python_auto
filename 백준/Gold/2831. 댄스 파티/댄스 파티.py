# https://www.acmicpc.net/problem/2831
def big_small_separate():
    big, small = [], []
    for x in map(int, input().split()):
        if x > 0:
            big.append(x)
        else:
            small.append(-x)

    big.sort()
    small.sort()
    return big, small


def get_pair(big, small):
    lenb, lens = len(big), len(small)
    bi, si = 0, 0
    cnt = 0

    while bi < lenb and si < lens:
        if big[bi] < small[si]:
            cnt += 1
            bi += 1
            si += 1
        else:
            si += 1

    return cnt


input()
bm, sm = big_small_separate()
bw, sw = big_small_separate()

print(get_pair(bm, sw) + get_pair(bw, sm))