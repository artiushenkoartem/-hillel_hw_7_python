"""2) написать функцию которая принимает в качестве аргумента номер месяца,
 в возвращает строку - время года, этого месяца"""
# create a function that should display the time of year
def seasons(month: int):
    # set the matching condition
    if month in [12, 1, 2]:
        return 'winter'
    elif month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    elif month in [9, 10, 11]:
        return 'autumn'
    # if the value does not fit the conditions, output it
    else:
        return 'There is no such month in the year'

print(seasons(13))
