t = input()

key = ord(t[0]) ^ ord('C')
print(''.join(map(lambda c: chr(ord(c) ^ key), t)))
