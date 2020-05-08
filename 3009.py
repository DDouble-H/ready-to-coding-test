import sys
x_=[]
y_=[]

for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_.append(x)
    y_.append(y)
for i in range(3):
    if x_.count(x_[i]) ==1:
        v1 = x_[i]
    if y_.count(y_[i]) ==1:
        v2 = y_[i]
print(v1, v2)