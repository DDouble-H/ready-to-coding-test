score_arr = []
for i in range(5):
    score =int(input())
    score_arr.append(score)
sum = 0
for score in score_arr:
    if score < 40 :
        score = 40
    sum += score
avg = int(sum//5)
print(avg)