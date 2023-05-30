def happy(tic):
    x=0
    y=0
    a = len(tic)
    if a%2==0:
        for i in range(0, a//2):
            x = x+int(tic[0])
            tic = tic[1:]
        for i in range(a // 2, a):
            y = y+int(tic[0])
            tic = tic[1:]
    else:
        return "Введите билет с четным количеством знаков."
    if x==y:
        return "Это счастливый билет!"
    return "Этот билет не является счастливым."

tic = str(input())
print(happy(tic))

