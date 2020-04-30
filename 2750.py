import sys
num = []
for i in range(int(sys.stdin.readline())):
    num.append(int(sys.stdin.readline()))
result = sorted(num)

for i in range(len(result)):
    print(result[i], end=' \n')