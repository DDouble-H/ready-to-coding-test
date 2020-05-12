import sys
word = []
sort_word = []

for _ in range(int(sys.stdin.readline())):
    word.append(sys.stdin.readline().rstrip())
set_word = list(set(word))

for j in set_word:
    sort_word.append((len(j), j))
sort_word.sort()

for l, w in sort_word:
    print(w)