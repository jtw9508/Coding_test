year = int(input())

def is_leap(year):
    if (year % 4) != 0:
        return 0
    elif (year % 100) == 0:
        if (year % 400) == 0:
            return 1
        else:
            return 0
    else:
        return 1
        
print(is_leap(year))