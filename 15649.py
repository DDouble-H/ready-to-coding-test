import sys
from itertools import permutations

n,m = map(int, sys.stdin.readline().split())

for i in permutations(range(1, n+1), m):
    print(' '.join(map(str, i)))