import sys
w = sys.stdin.readline()
count = 0
for i in w:
    if i == 'a':
        count += 1
    elif i == 'e':
        count += 1
    elif i == 'i':
        count +=1
    elif i == 'o':
        count +=1
    elif i == 'u':
        count +=1
print(count)
