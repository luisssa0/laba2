import random
f = 0
k = 0
while f < 3:
    a = random.randint(0,15)
    b = random.randint(0,15)
    print(a, '+', b, '=', end = " ")
    n = int(input())
    if a + b == n:
        print("Правильно!")
        k+=1
    else:
        f+=1
        print("Ответ неверный.")
print("Игра окончена. Правильных ответов: ", k)