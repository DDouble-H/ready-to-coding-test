from math import gcd
import sys

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split(' '))
    print(a*b//gcd(a,b))