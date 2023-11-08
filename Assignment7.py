#Assignment 7.1
def chop(list):
    if len(list) >= 2:
        del list[0]
        del list[-1]
    else:
        list.clear()

def middle(list):
    if len(list) >= 3:
        return list[1:-1]
    else:
        return []

list_1 = [1, 2, 3, 4]

print("my list before call chop function =>", list_1)
chop(list_1)
print("my list after call chop function =>", list_1)

my_list = [1, 2, 3, 4]

print("\nmy list before call middle function =>", my_list)
new_list = middle(my_list)
print("my list after call middle function =>", my_list)
print("new list after call middle function =>", new_list)
#Assignment 7.2
try:
    with open('romeo.txt', 'r') as file:
        unique_words = []
        for line in file:
            words = line.split()
            for word in words:
                if word not in unique_words:
                    unique_words.append(word)

        unique_words.sort()
        print(unique_words)
except FileNotFoundError:
    print("The 'romeo.txt' file was not found.")
except Exception as e:
    print("An error occurred:", e)

#Assignment 7.3
try:
    name = input("Enter the file name: ")
    with open(name, 'r') as file:
        send = []
        for line in file:
            if line.startswith('From '):
                words = line.split()
                if len(words) > 1:
                    sends = words[1]
                    print(send)
                    send.append(sends)
        
        print(f"Total {len(send)} lines were printed")
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print("An error occurred:", e)
#Assignment 7.4
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

print("Bye__")