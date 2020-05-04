import sys
N = list((sys.stdin.readline()))
N.sort(reverse=True)
for i in N:
    print(i, end='')