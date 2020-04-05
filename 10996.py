N = int(input())
a = N
b = N//2
for i in range(1, N+1):
    if a % 2 == 1: #
        print('* '* (a-b))
        print(' *'* b)
    else:
        print('* '* b)
        print(' *'* (a-b))