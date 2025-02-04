# https://www.acmicpc.net/problem/23284
def backtracking(stack: list, push: int, pops: list, rest: int):
    if not rest:
        print(' '.join(map(str, pops)))
        return

    # cant push
    if push > n:
        backtracking([], n, pops + stack[::-1], 0)
        return

    if stack:  # only can pop
        backtracking(stack[:-1], push, pops + [stack[-1]], rest-1)  # pop
    backtracking(stack + [push], push + 1, pops, rest-1)  # push


n = int(input())
backtracking([], 1, [], n << 1)