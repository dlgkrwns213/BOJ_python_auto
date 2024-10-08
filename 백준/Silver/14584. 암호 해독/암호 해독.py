import sys
input = sys.stdin.readline


def change_word(word, cnt):
    change_alphabet = lambda alphabet: chr((ord(alphabet) - ord('a') + cnt) % 26 + ord('a'))
    return ''.join(map(change_alphabet, word))


def find():
    for i in range(26):
        for new_word in map(lambda word: change_word(word, i), words):
            if new_word in code:
                return -i


if __name__ == '__main__':
    code = input().rstrip()
    n = int(input())
    words = [input().rstrip() for _ in range(n)]

    print(change_word(code, find()))