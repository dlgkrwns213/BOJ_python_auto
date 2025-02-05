for _ in range(int(input())):
    ipt = input()
    print(sum(map(int, ipt.split('+'))) if '+' in ipt else 'skipped')