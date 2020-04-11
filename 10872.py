import sys

def factorial(N):
    global n
    if N == 1:
        return
    elif N == 0:
        return
    n *= N
    N -= 1
    factorial(N)

N = int(sys.stdin.readline())
n = 1
factorial(N)
print(n)