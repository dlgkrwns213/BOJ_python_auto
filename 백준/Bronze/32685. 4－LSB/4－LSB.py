data = ''.join(map(lambda x: bin(x & 15)[2:].zfill(4), (int(input()) for _ in range(3))))

print(str(int(data, 2)).zfill(4))