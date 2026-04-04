import sys
input = sys.stdin.readline

n = int(input())
locations = [list(map(int, input().split())) for _ in range(n)]
locations.sort()

result = n
for i in range(n):
    b = locations[i][1] + 1

    below = []
    above = []

    for x, y in locations:
        if y < b:
            below.append((x, y))
        else:
            above.append((x, y))

    below.sort()
    above.sort()

    bi = 0
    bl = len(below)

    ai = 0
    al = len(above)

    for j in range(n):
        a = locations[j][0] + 1

        while bi < bl and below[bi][0] < a:
            bi += 1

        while ai < al and above[ai][0] < a:
            ai += 1

        result = min(result, max(bi, ai, bl-bi, al-ai))

print(result)