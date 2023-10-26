
def isLeapYear(year):
    divided_by_4 = year % 4 == 0
    divided_by_400 = year % 400 == 0
    not_divided_by_100 = year % 100 != 0

    is_leap_year = (divided_by_4 and not_divided_by_100) or divided_by_400
    return is_leap_year
