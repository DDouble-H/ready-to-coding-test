import sys
# for i in range(int(input())):
#     A, B = sys.stdin.readline().split()
#     A = int(A)
#     B = int(B)
#     print(A + B)

for i in range(int(input())):
    A, B = [int(n) for n in sys.stdin.readline().rstrip().split()]
    print(A+B)