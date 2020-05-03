import sys
num = []
for i in range(int(sys.stdin.readline())):
    num.append(int(sys.stdin.readline()))

result = sorted(num)
for i in result:
    print(i, end='\n')
