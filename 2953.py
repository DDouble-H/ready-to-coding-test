import sys
b = list()
for _ in range(5):
    a = list(map(int, sys.stdin.readline().split()))
    b.append(sum(a))
print(b.index(max(b))+1, max(b))