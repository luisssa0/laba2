students_languages = {
    "Иванов": {"английский", "французский", "немецкий"},
    "Петров": {"английский", "испанский", "итальянский", "китайский"},
    "Сидоров": {"английский", "немецкий", "китайский"},
    "Козлов": {"испанский", "китайский"},
    "Смирнова": {"французский", "немецкий", "китайский"},
    "Попова": {"английский", "испанский", "китайский"}
}


all_languages = set()
for languages in students_languages.values():
    all_languages.update(languages)


sorted_languages = sorted(all_languages)
print("Список всех языков, которые знают студенты:")
print(sorted_languages)


chinese_speakers = [name for name, languages in students_languages.items() if "китайский" in languages]
print("Студенты, знающие китайский язык:")
print(chinese_speakers)