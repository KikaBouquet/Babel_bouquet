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


d1 = "1701, 1, 1"
d2 = "0019, 3, 30"
d3 = "1700, 2, 29"
d4 = "2011, 3, 18"
d5 = "1200, 12, 12"
d6 = "0403, 9, 25"
d7 = "0000, 6, 1"


dateList = [d1, d2, d3, d4, d5, d6, d7]
dateList_withResult = [(d1, 18), (d2, 1), (d4, 21), (d5, 12), (d6, 5)]

i = 1
# test sans les résultats attendus
"""
for d in dateList:
    try:
        d = datetime.strptime(d, "%Y, %m, %d")
    except Exception as e:
        print(f"d{i}: {e}")
        d = None

    if d:
        result = get_century(d)
        print(f"d{i} : {result}")

 i = i + 1
"""

# test avec les résultats attendus
for f in dateList_withResult:

    year = f[0]
    try:
        date_to_test = datetime.strptime(year, "%Y, %m, %d")
    except Exception as e:
        print(f"d{i}: {e}")
        date_to_test = None

    if date_to_test:
        result = get_century(date_to_test)
        if f[1] == result:
            print(f"d{i} : PASSED")
        else:
            print(f"d{i} : ERROR")

    i = i + 1
