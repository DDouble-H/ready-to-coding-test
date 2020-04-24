import sys
arr = list(range(1,31))

for _ in range(28):
    arr.pop(arr.index(int(sys.stdin.readline())))

for i in arr:
    print(i)