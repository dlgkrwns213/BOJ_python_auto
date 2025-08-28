import sys
input = sys.stdin.readline

vowels_set = set("aeiouAEIOU")
for i in range(int(input())):
    sentence = input().rstrip()
    vowels = 0
    consonants = 0

    for ch in sentence:
        if ch.isalpha():
            if ch in vowels_set:
                vowels += 1
            else:
                consonants += 1
    print(consonants, vowels)