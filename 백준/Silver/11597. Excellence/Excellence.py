n = int(input())
scores = sorted(int(input()) for _ in range(n))

print(min(scores[i] + scores[-i-1] for i in range(n//2)))