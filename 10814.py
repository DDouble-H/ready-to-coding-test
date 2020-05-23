import sys
n = int(sys.stdin.readline())
num = []

for i in range(n):
    num.append(list(sys.stdin.readline().split()))

num.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(num[i][0], num[i][1])