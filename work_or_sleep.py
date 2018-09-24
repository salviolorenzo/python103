day = int(input('Day (0-6)'))
work = "Go to work."
sleep_in = "Sleep in."
statement = ""
if day >= 0 and day < 5:
    statement = work
elif day >= 5 and day <= 6:
    statement = sleep_in
else:
    statement = "Please enter a number between 0 and 6."
print (statement)