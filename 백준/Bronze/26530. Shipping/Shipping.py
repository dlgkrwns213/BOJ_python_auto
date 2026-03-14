for _ in range(int(input())):
    total = 0.0

    for _ in range(int(input())):
        name, q, price = input().split()
        total += int(q) * float(price)

    print(f"${total:.2f}")