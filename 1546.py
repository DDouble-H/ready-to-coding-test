import sys
N = int(sys.stdin.readline())
score = list(map(int, input().split()))
M = max(score)
new = 0
for i in range(len(score)):
    #new = (score[i]/M)*100
    new += (score[i]/M)*100
avg = (new/N)
print(avg)