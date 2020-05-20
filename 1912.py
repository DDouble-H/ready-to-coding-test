import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

sum_max = [num[0]]
for i in range(len(num)-1):
    sum_max.append(max(sum_max[i]+num[i+1], num[i+1]))
print(max(sum_max))