import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
result = list()
for i in range(M, N+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
        if count > 2:
            break
    if count == 2:
        result.append(i)
if len(result):
    print(sum(result))
    print(min(result))
else:
    print(-1)