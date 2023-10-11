#Assignment 4.1
def Grade(score):
    if score < 0 or score > 100:
        return "Error: Score is out of range"
    elif score >= 90:
        return "Grade is A"
    elif score >= 80:
        return "Grade is B"
    elif score >= 70:
        return "Grade is C"
    elif score >= 60:
        return "Grade is D"
    else:
        return "Grade is F"
    
if __name__ == '__main__':
    try:
        score = int(input("Enter a score between 0 and 100: "))
        expected_grade = Grade(score)
        print(expected_grade)
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value between 0 and 100.")

#Assignment 4.2
def computepay(hour, salary):
    if hour > 40:
        extra_time = hour - 40
        salary = (40 * rate) + (extra_time * rate * 1.5)
        return salary
    else:
        salary = hour * rate
        return salary

if __name__ == '__main__':
    try:
        hour = int(input("Enter Hour:"))
        rate = float(input("Enter rate: "))
        Final_Salary = computepay(hour,rate)
        print(Final_Salary)
    except ValueError:
        print("Please, Enter a numeric number")

#Assignment 4.3
def num_divide3(num):
    sum = 0
    for i in range(1,num + 1):
        if i % 3 == 0:
            sum += 1
    return sum

if __name__ == '__main__':
    while True:
        number_input = input("Enter a positive integer : ")
        if number_input == "done":
            break
        try:
            num = int(number_input)
            if num < 1:
                print("Enter a positive Number")
                
            else:
                Number = num_divide3(num)
                print("numbers divisible by 3 among numbers from 1 to ",num, ":", Number)
        except:
            print("Please enter a positive number")