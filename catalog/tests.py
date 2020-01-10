from django.datetime import datetime
from .utils import get_century

# Create your tests here.


def test_get_century(strDate):
    d1 = "1701, 1, 1"
    d2 = "0019, 3, 30"
    d3 = "1700, 2, 29"
    d4 = "2011, 3, 18"
    d5 = "1200, 12, 12"
    d6 = "0403, 9, 25"
    d7 = "0000, 6, 1"
    dateList_withResult = [(d1, 18), (d2, 1), (d4, 21), (d5, 12), (d6, 5)]

    i = 1
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
