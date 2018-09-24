day = int(input('Day (0-6)'))
mon = 'Monday'
tue = 'Tuesday'
wed = 'Wednesday'
thu = 'Thursday'
fri = "Friday"
sat = 'Saturday'
sun = 'Sunday'
day_of_week = ''

if day == 0:
    day_of_week = mon
elif day == 1:
    day_of_week = tue
elif day == 2:      
    day_of_week = wed
elif day == 3:
    day_of_week = thu
elif day == 4:
    day_of_week = fri
elif day == 5:
    day_of_week = sat
elif day == 6:
    day_of_week = sun
else: 
    day_of_week = "Please enter a number between 0-6."
print(day_of_week)
