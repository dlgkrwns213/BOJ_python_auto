import sys
input = sys.stdin.readline

num = int(input())
while True:
    ipt = input().rstrip()
    if ipt == '=':
        break

    if ipt == '+':
        num += int(input())
    elif ipt == '-':
        num -= int(input())
    elif ipt == '*':
        num *= int(input())
    elif ipt == '/':
        num //= int(input())

print(num)