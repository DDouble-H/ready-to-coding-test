import sys
a,b,v = map(int, sys.stdin.readline().split())
count = 0
v = v-a
if v % (a-b) == 0:
    count += (v//(a-b)+1)
else:
    count += (v//(a-b)+2)
print(count)