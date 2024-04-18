from math import lcm


def get_ans():
    if not d % p or not d % q:
        return d

    x = (d + p - 1) // p
    now = p * x
    mn = now
    for _ in range(x):
        now -= p
        cnt, rest = divmod(d - now, q)
        if not rest:
            return d

        now += (cnt+1) * q
        if mn == now:
            return mn
        mn = min(mn, now)

    return mn


d, p, q = map(int, input().split())
if p < q:
    p, q = q, p

print(get_ans())