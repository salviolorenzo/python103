bill = float(input('Bill amount? '))
service = input('Level of service? (good, fair, bad) ')
split = int(input('Split how many ways? '))
if service == 'good':
    tip = 0.2
elif service == 'fair':
    tip = 0.15
elif service == 'bad':
    tip = 0.10
else:
    print('Please enter one of the three service options.')
tip_amount = bill*tip
total = bill + tip_amount
per_person = total/split 
print("Tip amount: %.2f" %(tip_amount))
print('Total amount: %.2f' % (total))
print('Amount per person: %.2f' % (per_person))