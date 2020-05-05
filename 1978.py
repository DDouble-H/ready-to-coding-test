import sys
N = int(sys.stdin.readline())
num = sys.stdin.readline().split()
ans = 0
for nn in num:
    count = 0
    for i in range(1, int(nn)+1):
        if int(nn) % i == 0:
            count += 1
    if count == 2:
        ans += 1
print(ans)