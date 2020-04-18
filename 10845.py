from collections import deque

class queue_q:
    def __init__(self):
        self.queue = deque()

    def push(self, n):
        self.queue.append(n)

    def pop(self):
        if len(self.queue) != 0:
            return self.queue.popleft()
        else:
            return -1

    def size(self):
        return len(self.queue)

    def empty(self):
        if self.size() == 0:
            return 1
        return 0

    def front(self):
        if self.size():
            return self.queue[0]
        return -1

    def back(self):
        if self.size():
            return self.queue[-1]
        return -1

import sys
Q = queue_q()

for i in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split() # 1 or 2
    if cmd[0] == "push":
        Q.push(cmd[1])
    elif cmd[0] == "size":
        print(Q.size())
    elif cmd[0] == "empty":
        print(Q.empty())
    elif cmd[0] == "pop":
        print(Q.pop())
    elif cmd[0] == "front":
        print(Q.front())
    elif cmd[0] == "back":
        print(Q.back())