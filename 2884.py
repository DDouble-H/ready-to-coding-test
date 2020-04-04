H, M = input().split()
H = int(H)
M = int(M)

if 60 > M > 44:
    M = M - 45
    print(H, M)
else:
    M = M + 15
    if 0 < H < 24:
        H = H - 1
    else:
        H = 23
    print(H, M)
