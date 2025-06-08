def get_score(ipt: str) -> int:
    a, d, g = map(int, ipt.split())
    return a * (d + g) * (2 if a == d + g else 1)


print(max(map(get_score, (input() for _ in range(int(input()))))))