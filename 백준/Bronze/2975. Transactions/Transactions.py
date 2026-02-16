while True:
    b, t, a = input().split()
    b, a = int(b), int(a)

    if b == 0 and t == "W" and a == 0:
        break

    print("Not allowed" if t == "W" and b - a < -200 else b - a if t == "W" else b + a)