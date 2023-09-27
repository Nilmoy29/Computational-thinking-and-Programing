#Assignment 3.1
try:
    hour = int(input("Enter Hour:"))
    rate = float(input("Enter rate: "))
    if hour > 40:
        extra_time = hour - 40
        salary = (40 * rate) + (extra_time * rate * 1.5)
        print(salary)
    else:
        salary = hour * rate
        print(salary)
except:
    print("Error, please enter valid input")

#Assignment 3.2
try:
    score_input = int(input("Enter a score between 0 to 100: "))
    while score_input in range(0,101):
        if score_input >= 90:
            print("Grade is A")
            break
        elif score_input >= 80:
            print("Grade is B")
            break
        elif score_input >= 70:
            print("Grade is C")
            break
        elif score_input >= 60:
            print("Grade is D")
            break
        elif score_input < 60:
            print("Grade is F")
            break
except:
    print("Entered value is out of range")

#Assignment 3.3
sum_numbers = 0
Count = 0
while True:
    Input = input("Entter a number: ")
    if Input == "done":
        break
    try:
        Input = int(Input)
    except:
        print("Invalid input. Type a Number")
        continue
    sum_numbers += Input
    Count += 1
    
print("Sum of Numbers: ",sum_numbers)
print("Number of input: ",Count)
print("Avarage of Numbers: ",(sum_numbers//Count))







