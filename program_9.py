time=int(input('enter your time:'))
morning_start = 5
afternoon_start = 12
evening_start = 16  
night_start = 19

if morning_start <= time < afternoon_start:
    greeting = "Good Morning"
elif afternoon_start <= time < evening_start:
    greeting = "Good Afternoon"
elif evening_start <= time < night_start:
    greeting = "Good Evening"
else:
    greeting = "Good Night"
print(f'{greeting} current time is {time}')
