scores = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0, '+': 0.5}

s = input()
total = sum(map(lambda x: scores[x], s))

print(total / (len(s)-s.count('+')))