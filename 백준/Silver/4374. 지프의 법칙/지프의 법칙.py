import sys
from collections import defaultdict

input = sys.stdin.read
gap_line = input().strip().split("\n")

i = 0
case = True

while i < len(gap_line):
    if not case:
        print()
    case = False

    n = int(gap_line[i].strip())
    i += 1

    words = defaultdict(int)
    while i < len(gap_line) and gap_line[i].strip() != "EndOfText":
        line = gap_line[i].strip().lower()
        word = ""
        for s in line:
            if s.isalpha():
                word += s
            else:
                if word:
                    words[word] += 1
                    word = ""
        if word:
            words[word] += 1
        i += 1

    i += 1

    result = sorted([word for word, count in words.items() if count == n])

    if result:
        for word in result:
            print(word)
    else:
        print("There is no such word.")
