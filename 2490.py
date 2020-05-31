import sys
for i in range(3):
    s = list(map(int, sys.stdin.readline().split()))
    if s.count(0) == 1:
        print('A')
    elif s.count(0) == 2:
        print('B')
    elif s.count(0) == 3:
        print('C')
    elif s.count(0) == 4:
        print('D')
    elif s.count(0) == 0:
        print('E')