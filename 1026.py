import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
s = 0
for _ in range(len(A)):
    s += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))
print(s)