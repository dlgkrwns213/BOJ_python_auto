def dfs(word, make, made, idx=0):
    if len(make) == k:
        made.add(make)
        return
    if idx == len(word):
        return

    dfs(word, make, made, idx+1)
    dfs(word, make+word[idx], made, idx+1)


x = input()
y = input()
z = input()
k = int(input())

xmade, ymade, zmade = set(), set(), set()
dfs(x, '', xmade)
dfs(y, '', ymade)
dfs(z, '', zmade)

ans = (xmade & ymade) | (ymade & zmade) | (zmade & xmade)
print('\n'.join(sorted(ans)) if ans else '-1')