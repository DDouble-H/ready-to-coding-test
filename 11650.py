import sys
n = int(sys.stdin.readline())
num = []
for i in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))
    num.append([a, b])
num = sorted(num)

for i in range(n):
    print(num[i][0], num[i][1])

