# https://www.acmicpc.net/problem/2502
def get_ans(a, b, k):
    for x in range(1, k):
        rest = k - a*x
        if rest % b == 0:
            return x, rest//b


d, k = map(int, input().split())
today, yesterday = [1, 1], [0, 1]
for _ in range(d-3):
    a, b = today
    c, d = yesterday
    today = [a+c, b+d]
    yesterday = [a, b]

a, b = today
x, y = get_ans(a, b, k)
print(x, y, sep='\n')