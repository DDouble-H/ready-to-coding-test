N = int(input())
for i in range(N-1, -1, -1):
    print(' '*i + '*'*(N-i))
for i in range(1, N):
    print(' ' * i + '*' * (N - i))