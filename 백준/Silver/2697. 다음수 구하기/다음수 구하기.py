for _ in range(int(input())):
    num = input()
    small = chr(ord('0')-1)

    behinds, change = [small], None
    for bit in num[::-1]:
        if behinds[-1] > bit:
            behinds.append(bit)
            change = min([b for b in behinds if behinds[-1] < b], default=small)
            break

        behinds.append(bit)

    if not change:
        print('BIGGEST')
        continue

    ans = num[:-len(behinds)+1] + change
    behinds.remove(change)
    print(ans+''.join(sorted(behinds[1:])))