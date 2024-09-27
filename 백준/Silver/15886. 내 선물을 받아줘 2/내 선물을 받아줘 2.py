n = int(input())
board = ['E']

for x in input():
    if x == board[-1]:
        continue
    board.append(x)

print(len(board)>>1)