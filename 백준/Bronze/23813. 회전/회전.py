n = input()
print(sum(map(lambda i: int(n[i:]+n[:i]), range(len(n)))))