input()
numbers = list(map(int, input().split()))

print(len(bin(max(numbers))) - 3 + sum(map(lambda num: bin(num).count('1'), numbers)))