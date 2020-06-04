import sys
n = sys.stdin.readline().split()
s = list()
for i in n:
    s.append((int(i) ** 2))
s = sum(s)
print(s%10)