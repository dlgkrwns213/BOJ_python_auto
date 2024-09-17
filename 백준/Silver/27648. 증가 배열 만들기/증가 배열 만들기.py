n, m, k = map(int, input().split())
print('NO' if n+m > k+1 else 'YES\n'+'\n'.join(map(lambda i: ' '.join(map(lambda j: str(i+j+1), range(m)), ), range(n))))