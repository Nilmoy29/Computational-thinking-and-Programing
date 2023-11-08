number = []
while True:
    user_input = input("Please enter an integer: ")
    if user_input == 'done':
        break
    try:
        numbers = int(user_input)
        number.append(numbers)
        average = sum(number) / len(number)
        print(f"{number}, average = {average:.2f}")
    except ValueError:
        print("Invalid input. Please enter an integer or 'done' to exit.")

print("Bye")






