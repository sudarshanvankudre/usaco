"""
ID: sudarsh11
LANG: PYTHON3
TASK: friday
"""

def is_leap(year):
    if is_century(year) and year % 400 == 0:
        return True
    elif not is_century(year) and year % 4 == 0:
        return True
    return False

def is_century(year):
    return year % 100 == 0

def is_feb(month):
    return month == 2

def is_thirty(month):
    return month == 4 or month == 6 or month == 11 or month == 9

def days_gen():
    curr = 0
    while True:
        yield curr
        curr = (curr + 1) % 7

days = days_gen()
counts = [0 for _ in range(7)]
with open("friday.in", 'r') as fin:
    N = int(fin.readline())

for year in range(1900, 1900 + N):
    for month in range(1, 13):
        if is_leap(year) and is_feb(month):
            for date in range(1, 30):
                day = next(days)
                if date == 13:
                    counts[(day + 2) % 7] += 1
        elif is_feb(month):
            for date in range(1, 29):
                day = next(days)
                if date == 13:
                    counts[(day + 2) % 7] += 1
        elif is_thirty(month):
            for date in range(1, 31):
                day = next(days)
                if date == 13:
                    counts[(day + 2) % 7] += 1
        else:
            for date in range(1, 32):
                day = next(days)
                if date == 13:
                    counts[(day + 2) % 7] += 1
with open("friday.out", 'w') as fout:
    output = "".join(map(lambda x: str(x) + " ", counts)).rstrip()
    fout.write(output + "\n")
