burger = []
drink = []
for i in range(3):
    bur = int(input())
    burger.append(bur)
for j in range(2):
    dri = int(input())
    drink.append(dri)
print(min(burger) + min(drink) - 50)