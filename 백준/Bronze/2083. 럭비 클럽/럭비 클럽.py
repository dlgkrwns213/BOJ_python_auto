while True:
    ipt = input().split()
    if ipt == ['#', '0', '0']:
        break

    name = ipt[0]
    age, weight = map(int, ipt[1:])

    print(f"{name} {'Senior' if age > 17 or weight >= 80 else 'Junior'}")