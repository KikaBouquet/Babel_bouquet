from datetime import datetime


def get_century(date_birth):
    century_birth = 0

    if date_birth:
        year = date_birth.year
        str_year = str(year)

        if len(str_year) <= 2:
            century_birth = 1

        else:
            century_birth = year // 100

            if year % 100 != 0:
                century_birth = century_birth + 1

    return century_birth
