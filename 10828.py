# Q.10828(스택)
import sys
class stack:
    def __init__(self):
        self.stack = []
        self.len = 0

    def push(self, N):
        self.stack.append(N)
        self.len += 1

    def pop(self):
        if self.size() == 0:
            return -1
        delete = self.stack[self.len-1]
        del self.stack[self.len-1]
        self.len -= 1
        return delete

    def empty(self):
        if self.len == 0:
            return 1
        return 0

    def size(self):
        return self.len

    def top(self):
        if self.size() == 0:
            return -1
        return self.stack[-1]


if __name__ == '__main__':

    input=sys.stdin.readline

    N = int(input())
    S = stack()

    while(N > 0):
        N -= 1
        Input = input().split()

        word = Input[0]

        if word == 'quit' or word == 'q':
            break
        elif word == 'push':
            S.push(Input[1])
        elif word == 'pop':
            print(S.pop())
        elif word == 'empty':
            print(S.empty())
        elif word == 'size':
            print(S.size())
        elif word == 'top':
            print(S.top())
        else:
            print('Command Not Found')