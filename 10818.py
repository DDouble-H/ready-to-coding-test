import sys
N = int(sys.stdin.readline())
arr = [int(N) for N in sys.stdin.readline().split()]

# arr = []
# for N in sys.stdin.readline().split():
#     arr.append(int(N))

print(min(arr), max(arr))
