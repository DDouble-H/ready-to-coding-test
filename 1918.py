# Q.1918(후위 표기식)
def priority(x):
    if x == '*' or x == '/':
        return 2
    elif x == '+' or x == '-':
        return 1
    elif x == '(' or x == ')':
        return 0
    return -1

def solution():
    stack = []
    Input = input()
    result = ''
    for c in Input:
        p = priority(c)
        if c == '+' or c == '-' or c == '*' or c == '/':
            while stack and priority(stack[-1]) >= p:
                result += stack.pop()
            stack.append(c)
            continue
        elif c == '(':
            stack.append(c)
            continue
        elif c == ')':
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop()
            continue
        result += c
    while stack:
        result += stack.pop()
    print(result)


if __name__ == '__main__':
    solution()
