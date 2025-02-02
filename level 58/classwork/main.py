#1

import calendar
def is_leap_year(year):
    return calendar.isleap(year)


#2

def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])


#3

def shorten_to_date(long_date):
    return long_date.split(',')[0]

#4

def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower()) 

#5

def what_century(year):
    n = (int(year) - 1) // 100 + 1
    return str(n) + ("th" if n < 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))