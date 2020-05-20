import sys

n = int(sys.stdin.readline())
num = []
for i in range(n):
    a,b = list(map(int, sys.stdin.readline().split()))
    ss = [b, a]
    num.append(ss)
num = sorted(num)

for i in range(n):
    print(num[i][1], num[i][0])