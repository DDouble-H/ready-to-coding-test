# Q.10799(쇠막대기)
import sys
arr = list(sys.stdin.readline())
S = []
prev = None
count = 0
for i in range(len(arr)):
    if arr[i] == '(':
        S.append(arr[i])
    elif prev == '(' and arr[i] == ')':
        S.pop()
        count += len(S)
    elif prev == ')' and arr[i] == ')':
        count += 1
        S.pop()
    prev = arr[i]
print(count)

