import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
print(min(a)*max(a))