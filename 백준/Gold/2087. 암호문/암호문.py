# https://www.acmicpc.net/problem/17305
import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
want = int(input())

left = n >> 1
make = {}
for i in range(1 << left):
    bitstring = format(i, f'0{left}b')
    make[sum(map(lambda x: numbers[x] if bitstring[x] == '1' else 0, range(left)))] = bitstring

right = n - left
for i in range(1 << right):
    bitstring = format(i, f'0{right}b')
    find = want - sum(map(lambda x: numbers[left+x] if bitstring[x] == '1' else 0, range(right)))
    if find in make:
        print(make[find] + bitstring)
        break