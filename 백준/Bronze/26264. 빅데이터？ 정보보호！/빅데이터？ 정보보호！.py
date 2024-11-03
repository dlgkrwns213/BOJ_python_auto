n = int(input())
s = input().count('security')
b = n - s
print('bigdata? security!' if b == s else 'security!' if s > b else 'bigdata?')