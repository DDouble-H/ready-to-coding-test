import sys

for _ in range(int(sys.stdin.readline())):
    num, s = sys.stdin.readline().split()
    result = ''
    print(result)
    for i in s:
        result += i * int(num)
    print(result)