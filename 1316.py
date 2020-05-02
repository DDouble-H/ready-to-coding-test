import sys
ans = 0

for i in range(int(sys.stdin.readline())):
    word = sys.stdin.readline().split()
    for j in range(len(word)):
        if j != len(word)-1:
            if word[j] == word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                break
        else:
            ans += 1
print(ans)