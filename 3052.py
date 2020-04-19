import sys
n = []
m = []
for i in range(10):
    n.append(int(sys.stdin.readline()))
for j in n:
    s = j % 42
    if s not in m:
        m.append(s)
print(len(m))
