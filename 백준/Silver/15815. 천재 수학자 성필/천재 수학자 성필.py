stack = []
for x in input():
    if x.isdigit():
        stack.append(x)
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(eval(f"{b}{x if x != '/' else '//'}{a}"))

print(stack.pop())