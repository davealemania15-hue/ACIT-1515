import dow

dow.makeCalendar()


def getDayOfTheWeekForUserDate():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))

    days_of_the_week = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",]

    day_number = dow.getDayOfTheWeek(year, month, day)
    print(days_of_the_week[day_number])


getDayOfTheWeekForUserDate()