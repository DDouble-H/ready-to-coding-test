import sys
s = sys.stdin.readline().rstrip('\n').split(' ')
if s == sorted(s):
    print('ascending')
elif s == sorted(s, reverse=True):
    print('descending')
else:
    print('mixed')