def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(leap_year_resutl,month):

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year_resutl == True:
        return f"leap Year, {month_days[month]}"
    else:
        return f"Not leap year {month_days[month]}"

day
# 🚨 Do NOT change any of the code below
def main():
    year = int(input("Enter a year: "))
    leap_year_resutl = is_leap(year)

    month = int(input("Enter a month: "))
    days = days_in_month(leap_year_resutl,month)
    print(days)


main()
