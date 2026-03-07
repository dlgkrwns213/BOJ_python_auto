stroke = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

total = sum(stroke[ord(c)-65] for c in input())
print("I'm a winner!" if total % 2 else "You're the winner?")