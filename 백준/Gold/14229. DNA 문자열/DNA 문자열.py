# https://www.acmicpc.net/problem/14229
from itertools import product


def find_missing_dna(S):
    S_set = set(S[i:j] for i in range(len(S)) for j in range(i+1, min(i+6, len(S)+1)))  # 길이 5까지만 검사

    for length in range(1, 8):
        for dna in product("ACGT", repeat=length):
            dna_str = "".join(dna)
            if dna_str not in S_set:
                return dna_str


print(find_missing_dna(input()))