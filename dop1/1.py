synonyms = {}
with open('synonyms.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            word, synonyms_str = line.split(' - ')
            synonyms_list = synonyms_str.split(';')
            synonyms[word] = synonyms_list

while True:
    word = input('Введите слово для замены: ')
    if word.lower() == 'exit':
        break
    if word in synonyms:
        synonyms_list = synonyms[word]
        print(f'Найдены следующие синонимы: {", ".join(synonyms_list)}')
        replace_word = input('Хотите заменить слово на один из синонимов? (y/n): ')
        if replace_word.lower() == 'y':
            new_word = input('Выберите синоним из списка или введите свое слово: ')
            if new_word in synonyms_list:
                word = new_word
            else:
                synonyms_list.append(new_word)
                synonyms[word] = synonyms_list
                with open('synonyms.txt', 'a') as f:
                    f.write(f'\n{word} - {"; ".join(synonyms_list)}')
                    print(f'Слово "{new_word}" добавлено в базу синонимов')
        else:
            print(f'Слово "{word}" не изменено')
    else:
        print(f'Слово "{word}" не найдено в базе синонимов')
