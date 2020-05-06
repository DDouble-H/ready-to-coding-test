N, M = map(int, input().split())
ans =''
for i in range(1, (N*M)+1):
    if i%M==0:
        ans += str(i) +'\n'
    else:
        ans += str(i) + ' '
print(ans)