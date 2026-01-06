n = int(input())
x = int(input())
opens = [0, 1, 0, 1] if x else [1, 0, 1, 0]
if n >= 6:
    print('Love is open door')
else:
    print('\n'.join(map(str, opens[:n-1])))