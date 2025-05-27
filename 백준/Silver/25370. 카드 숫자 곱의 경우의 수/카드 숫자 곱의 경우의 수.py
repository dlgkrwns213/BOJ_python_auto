def backtracking(count, now):
    if count == n:
        number.add(now)
        return

    for i in range(1, 10):
        backtracking(count+1, now*i)

n = int(input())
number = set()
backtracking(0, 1)
print(len(number))