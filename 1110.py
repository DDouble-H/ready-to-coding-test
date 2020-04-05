N = num = int(input())
count = 0
while True:
    nn = N // 10
    n = N % 10
    sum = nn+n
    count += 1
    N = int(str(N %10) + str(sum %10))
    if N == num:
        break
print(count)