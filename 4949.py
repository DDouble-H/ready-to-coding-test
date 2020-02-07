# Q.4949(균형잡힌세상)

while True:
    string = input()
    stack = []
    if string == ".":
        break
    exp = True
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                exp = False
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                exp = False
                break
        elif i == ']':
            if len(stack) == 0:
                exp = False
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                exp = False
                break
    if len(stack) == 0 and exp:
        print("yes")
    else:
        print("no")
