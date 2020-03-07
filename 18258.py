# Q.18258(큐2)
import sys
from collections import deque
N = int(sys.stdin.readline())
Q = deque([])

for i in range(N):
    S = sys.stdin.readline().split()
    if S[0] == 'push':
        Q.append(S[1])
    elif S[0] == 'pop':
        if not Q:
            print(-1)
        else:
            print(Q.popleft())
    elif S[0] == 'size':
        print(len(Q))
    elif S[0] == 'empty':
        if not Q:
            print(1)
        else:
            print(0)
    elif S[0] == 'front':
        if not Q:
            print(-1)
        else:
            print(Q[0])
    elif S[0] == 'back':
        if not Q:
            print(-1)
        else:
            print(Q[-1])