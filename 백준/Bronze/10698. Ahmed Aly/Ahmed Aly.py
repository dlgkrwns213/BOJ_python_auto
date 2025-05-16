for i in range(int(input())):
    x, y = input().split("=")
    print(f"Case {i+1}: {'YES' if eval(x) == int(y) else 'NO'}")