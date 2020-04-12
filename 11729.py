import sys
N = int(sys.stdin.readline())

def hanoi(N, A, B, C):
    if N == 1:
        print(A, C)
    else:
        hanoi(N - 1, A, C, B)
        print(A, C)
        hanoi(N - 1, B, A, C)
k = 1
for i in range(N - 1):
    k = k * 2 + 1
print(k)
hanoi(N, 1, 2, 3)