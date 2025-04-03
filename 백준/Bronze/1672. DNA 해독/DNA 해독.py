change = {
    ('A', 'A'): 'A',
    ('A', 'G'): 'C',
    ('A', 'C'): 'A',
    ('A', 'T'): 'G',
    ('G', 'A'): 'C',
    ('G', 'G'): 'G',
    ('G', 'C'): 'T',
    ('G', 'T'): 'A',
    ('C', 'A'): 'A',
    ('C', 'G'): 'T',
    ('C', 'C'): 'C',
    ('C', 'T'): 'G',
    ('T', 'A'): 'G',
    ('T', 'G'): 'A',
    ('T', 'C'): 'G',
    ('T', 'T'): 'T',
}

n = int(input())
dna = list(input())

for _ in range(n-1):
    a, b = dna.pop(), dna.pop()
    dna.append(change[(a, b)])

print(*dna)