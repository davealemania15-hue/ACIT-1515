def isLeapYear(year):
    #Julian Calendar
    year %4 = 0
        return True
        else:
            return False
    

def getDayOfTheWeek(year, month, day):
    #Step 1
    last_two_dights = year % 100
    how_many_twelves = last_two_dights // 12

    #Step 2
    remainder = last_two_dights % 12

    #Step 3
    how_many_fours = remainder // 4

    Step 4
    total = how_many_twelves + remainder + how_many_fours + day

    Step 5
    month_codes = [0, 1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4]
    total += month_codes[month - 1]

    #leap year
    if isLeapYear(year) and (month == 1 or month == 2):
        total -= 1

    #the special offsets
    if year >= 2000 and year < 2100:
        total += 6

    #Step 6
    day_of_the_week = total % 7

    return day_of_the_week

def makeCalendar(): 
    days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_of_week = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
    
    year = 2026

    
    for month in range(1, 13):
        num_days = days_in_months[month]
        
        
        for day in range(1, num_days + 1):
            day_number = getDayOfTheWeek(year, month, day)
            day_name = days_of_week[day_number]
            
           
            print(f"{month}-{day}-{year} is a {day_name}.")

