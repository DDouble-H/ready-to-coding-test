# Q.9012(괄호)
for i in range(int(input())):
    vps = list(input())
    while len(vps) != 0:
        if vps[0] == ')' or vps[-1] == '(':
            print('NO')
            break
        else:
            if '(' and ')' in vps:
                vps.remove('(')
                vps.remove(')')
            else:
                print('NO')
                break
    if len(vps) == 0:
        print('YES')