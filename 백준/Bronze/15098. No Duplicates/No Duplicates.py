ans = "yes"
seen = set()

for word in input().split():
    if word in seen:
        ans = "no"
        break
    seen.add(word)

print(ans)