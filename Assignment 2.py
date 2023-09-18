#Assignment 2.1
Hour_input = int(input("Enter Hour: "))
print(Hour_input)
rate_input = float(input("Enter rate: "))
print(rate_input)
Calculate_Salary = Hour_input*rate_input
print("Salary; ",Calculate_Salary)

#Assignment 2.2
Celsius_input = int(input("Enter Celsius Temperature: "))
Fahrenheit_Temperature = Celsius_input*9/5+32
print("Fahrenheit Temperature: ",Fahrenheit_Temperature)

#Assignment 2.3
Second_input = int(input("Enter Seconds: "))
hours = int(Second_input/3600)
minutes = int((Second_input%3600)/60)
remaning_seconds = int(Second_input%60)
print(Second_input," seconds is",hours, "hours,",minutes," minutes",remaning_seconds, " seconds.")
