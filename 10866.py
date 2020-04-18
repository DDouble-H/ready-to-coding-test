# Q.10866(덱)
import sys
from collections import deque
class Deque_10866:
    def __init__(self):
        self.DE = deque()

    def push_front(self, N):
        self.DE.insert(0, N)

    def push_back(self, N):
        self.DE.append(N)

    def pop_front(self):
        if self.size():
            return self.DE.popleft()
        return -1

    def pop_back(self):
        if self.size():
            return self.DE.pop()
        return -1

    def size(self):
        return len(self.DE)

    def empty(self):
        if self.size():
            return 0
        return 1

    def front(self):
        if self.size():
            return self.DE[0]
        return -1

    def back(self):
        if self.size():
            return self.DE[-1]
        return -1


if __name__ == '__main__':
    import sys
    D = Deque_10866()

    for i in range(int(sys.stdin.readline())):
        cmd = sys.stdin.readline().split()

        if cmd[0] == 'push_back':
            D.push_back(cmd[1])
        elif cmd[0] == 'push_front':
            D.push_front(cmd[1])
        elif cmd[0] == 'front':
            print(D.front())
        elif cmd[0] == 'back':
            print(D.back())
        elif cmd[0] == 'size':
            print(D.size())
        elif cmd[0] == 'empty':
            print(D.empty())
        elif cmd[0] == 'pop_front':
            print(D.pop_front())
        elif cmd[0] == 'pop_back':
            print(D.pop_back())