import sys

for i in range(int(sys.stdin.readline())):
    score = 0
    t_score = 0
    ox = list(sys.stdin.readline())
    for j in range(len(ox)):
        if ox[j] == 'O':
            score += 1
            t_score += score
        else:
            score = 0
    print(t_score)