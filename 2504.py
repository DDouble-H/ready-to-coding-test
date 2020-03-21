# Q.2504(괄호의 값)

import sys
Input = sys.stdin.readline().rstrip()
stack = list()
for i in Input:
    if i == ")":
        t = 0
        while stack:
            sp = stack.pop()
            if sp == "(":
                if t == 0:
                    stack.append(2)
                else:
                    stack.append(2 * t)
                break
            elif sp == "[":
                print("0")
                exit(0)
            else:
                if t == 0:
                    t = int(sp)
                else:
                    t = t + int(sp)
    elif i == "]":
        t = 0
        while stack:
            sp = stack.pop()
            if sp == "[":
                if t == 0:
                    stack.append(3)
                else:
                    stack.append(3 * t)
                break
            elif sp == "(":
                print("0")
                exit(0)
            else:
                if t == 0:
                    t = int(sp)
                else:
                    t = t + int(sp)
    else:
        stack.append(i)

result = 0
for i in stack:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        result += i
print(result)