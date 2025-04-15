words = list(input())
for _ in range(int(input())):
    a, b = map(int, input().split())
    words[a], words[b] = words[b], words[a]
print(''.join(words))