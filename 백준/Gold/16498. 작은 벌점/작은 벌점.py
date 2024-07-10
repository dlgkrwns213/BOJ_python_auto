# https://www.acmicpc.net/problem/16498
def is_possible(now):
    ai, bi, ci = 0, 0, 0
    while ai < a_len and bi < b_len and ci < c_len:
        a_card, b_card, c_card = a_cards[ai], b_cards[bi], c_cards[ci]
        mn, mx = min(a_card, b_card, c_card), max(a_card, b_card, c_card)
        if mx - mn <= now:
            return True

        if mn == a_card:
            ai += 1
        elif mn == b_card:
            bi += 1
        else:
            ci += 1

    return False


a, b, c = map(int, input().split())
a_cards = sorted(map(int, input().split()))
b_cards = sorted(map(int, input().split()))
c_cards = sorted(map(int, input().split()))

a_len, b_len, c_len = len(a_cards), len(b_cards), len(c_cards)
left, right = 0, max(a_cards[-1], b_cards[-1], c_cards[-1])
while left < right:
    mid = left + right >> 1
    if is_possible(mid):
        right = mid
    else:
        left = mid + 1

print(left)