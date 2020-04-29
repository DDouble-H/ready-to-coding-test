import sys
#t = int(input())
#N = list(input())
t = int(sys.stdin.readline().rstrip()) # .rstrip() > 마지막에 있는 \n (엔터) 제거
N = list(sys.stdin.readline().rstrip())

ans = 0
for i in range(len(N)):
    ans += int(N[i])
print(ans)


# sys.stdin.readline() > 사용자가 입력한 값을 그대로 입력받음 ("A B C D E\n")
# sys.stdin.readline().rstrip() > 위의 사항을 그대로 수행 > \n 제거 ("A B C D E")
# sys.stdin.readline().rstrip().split() > 위의 사항을 그대로 수행 > 공백을 기준으로 분할 (["A","B","C","D","E"])

# [int(n) for n in sys.stdin.readline().rstrip().split()] > 공백을 기준으로 숫자가 여러개 입력될때 (리스트)
# list(map(int, sys.stdin.readline().rstrip().split())) > 위코드와 기능적으로 같음

# int(sys.stdin.readline().rstrip()) > 입력된 값을 숫자로 바꿈 (정수)
