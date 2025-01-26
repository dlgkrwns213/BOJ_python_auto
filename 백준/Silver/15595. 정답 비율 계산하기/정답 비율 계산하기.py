import sys
from collections import defaultdict
input = sys.stdin.readline

submission, correct = defaultdict(int), set()
for _ in range(int(input())):
    _, userID, result, *_ = input().split()
    if userID == 'megalusion':
        continue

    if userID not in correct:
        submission[userID] += 1
        if result == '4':
            correct.add(userID)

count = sum(map(lambda userID: submission[userID] if userID in correct else 0, submission))
print(100 * len(correct) / count if count else .0)