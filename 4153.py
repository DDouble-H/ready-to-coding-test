import sys
while True:
    sss = list(map(int, sys.stdin.readline().split()))
    if sum(sss) == 0:
        break
    d = max(sss)
    sss.remove(d)
    if (d**2) == ((sss[0] ** 2)+(sss[1]**2)):
        print('right')
    else:
        print('wrong')