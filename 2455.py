import sys
n = [0]
for i in range(4):
    a, b = map(int, sys.stdin.readline().split())
    s = a+b
    n.append(n[-1]-a+b)
print(max(n))