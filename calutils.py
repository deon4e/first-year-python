# Modules for Calutils
# By Deon Fourie
# 24 March

odd_months = (1, 3, 5, 7, 8, 10, 12)
even_months = (4, 6, 9, 11)


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False

def month_name(number):

    if number == 1:
        number = "January"
        return number
    elif number == 2:
        number = "February"
        return number
    elif number == 3:
        number = "March"
        return number
    elif number == 4:
        number = "April"
        return number
    elif number == 5:
        number = "May"
        return number
    elif number == 6:
        number = "June"
        return number
    elif number == 7:
        number = "July"
        return number
    elif number == 8:
        number = "August"
        return number
    elif number == 9:
        number = "September"
        return number
    elif number == 10:
        number = "October"
        return number
    elif number == 11:
        number = "November"
        return number
    elif number == 12:
        number = "December"
        return number

def days_in_month(month_number, year):
    numdays = ""
    if is_leap_year(year) is True:
        if month_number in odd_months:
            numdays = "31"
            return numdays
        elif month_number in even_months:
            numdays = "30"
            return numdays
        elif month_number == 2:
            numdays = "29"
            return numdays
    else:
        if month_number in odd_months:
            numdays = "31"
            return numdays
        elif month_number in even_months:
            numdays = "30"
            return numdays
        elif month_number == 2:
            numdays = "28"
            return numdays


def first_day_of_year(year):
    x = (year - 1)
    day = 1
    day = day + (5 * (x % 4))
    day = day + (4 * (x % 100))
    day = day + (6 * (x % 400))
    day = day % 7
    return day

def first_day_of_month(month_number,year):
    if is_leap_year(year) is True:
        if month_number == 1:
            month_number = 0
        elif month_number == 2:
            month_number = 3
        elif month_number == 3:
            month_number = 4
        elif month_number == 4:
            month_number = 0
        elif month_number == 5:
            month_number = 2
        elif month_number == 6:
            month_number = 5
        elif month_number == 7:
            month_number = 0
        elif month_number == 8:
            month_number = 3
        elif month_number == 9:
            month_number = 6
        elif month_number == 10:
            month_number = 1
        elif month_number == 11:
            month_number = 4
        elif month_number == 12:
            month_number = 6
        x = year - 1
        day = 1
        day = day + month_number
        day = day + (5 * (x % 4))
        day = day + (4 * (x % 100))
        day = day + (6 * (x % 400))
        day = day % 7

        return day
    else:
        if month_number == 1:
            month_number = 0
        elif month_number == 2:
            month_number = 3
        elif month_number == 3:
            month_number = 3
        elif month_number == 4:
            month_number = 6
        elif month_number == 5:
            month_number = 1
        elif month_number == 6:
            month_number = 4
        elif month_number == 7:
            month_number = 6
        elif month_number == 8:
            month_number = 2
        elif month_number == 9:
            month_number = 5
        elif month_number == 10:
            month_number = 0
        elif month_number == 11:
            month_number = 3
        elif month_number == 12:
            month_number = 5
        x = year - 1
        day = 1
        day = day + month_number
        day = day + (5 * (x % 4))
        day = day + (4 * (x % 100))
        day = day + (6 * (x % 400))
        day = day % 7

        return day














