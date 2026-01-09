
n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
words = []
for i in range(n):
    make = []
    for x in board[i]:
        if x == '#':
            if len(make) >= 2:
                words.append(''.join(make))
            make = []
        else:
            make.append(x)

    if len(make) >= 2:
        words.append(''.join(make))

for j in range(m):
    make = []
    for i in range(n):
        x = board[i][j]
        if x == '#':
            if len(make) >= 2:
                words.append(''.join(make))
            make = []
        else:
            make.append(x)

    if len(make) >= 2:
        words.append(''.join(make))

words.sort()
print(words[0])