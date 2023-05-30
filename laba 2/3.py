word=input('Введите слово: ')
for i in word:
    if i=="ф":
        print('Ого! Это редкое слово!')
        break
    else:
        print('Эх, это не очень редкое слово...')
        break
