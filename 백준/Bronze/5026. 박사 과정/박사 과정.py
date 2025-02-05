for _ in range(int(input())):
    ipt = input()
    if ipt == 'P=NP':
        print('skipped')
    else:
        print(sum(map(int, ipt.split('+'))))
