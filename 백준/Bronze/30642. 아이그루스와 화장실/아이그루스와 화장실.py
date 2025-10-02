n = int(input())
t = 1 if input() == 'annyong' else 0
k = int(input())

if k % 2 == t:
    print(k)
else:
    print(k-1 if k > 1 else k+1)