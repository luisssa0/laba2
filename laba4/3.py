def magic_date(date):
    return int(date[:2]) * int(date[3:5]) == int(date[8:10])
date = input()
print(magic_date(date))