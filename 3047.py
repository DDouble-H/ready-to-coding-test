import sys
a = list(map(int,sys.stdin.readline().split()))
abc = sys.stdin.readline()
a = sorted(a)
for i in abc:
    if i =='A':
        print(a[0], end=' ')
    elif i =='B':
        print(a[1], end=' ')
    elif i =='C':
        print(a[2], end=' ')