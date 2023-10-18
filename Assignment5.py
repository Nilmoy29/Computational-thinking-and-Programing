#Assignment 5.1
while True:
    word_input = input("Please enter two words: ")
    if word_input == "done":
        print("Bye")
        break
    word_split = word_input.split()
    if len(word_split) == 2:
        output = min(word_split)
    elif len(word_split) == 1:
        print("type two words")
        continue
    print(f"{output} comes first")

#Assignment 5.2

input_string = input("Enter a string: ")
reverse= len(input_string) - 1
while reverse >= 0:
    print(input_string[reverse])
    reverse-= 1

#Assignment 5.3

user_input = input("Please Enter a string: ")
uppercase = 0
lowercase = 0
numbers = 0
others = 0
for letter in user_input:
    if letter.isupper():
        uppercase += 1
    elif letter.islower():
        lowercase += 1
    elif letter.isnumeric():
        numbers += 1
    else:
        others += 1
print(f"Uppercase Letters: {uppercase}")
print(f"Lowercase Letters: {lowercase}")
print(f"Numbers: {numbers}")
print(f"Others: {others}")

#Assignment 5.4
while True:    
    input_string = input("Please enter string: ")
    if input_string == "done":
        break
    list_string = list(input_string)
    for i in list_string:
        if i == ",":
            list_string.remove(",")
        elif i == ".":
            list_string.remove(",")
        elif i == "!":
            list_string.remove("!")
        elif i == ":":
            list_string.remove(":")
        elif i == "?":
            list_string.remove("?")
            
    new_string = "".join(list_string)
    final_string = new_string.upper()
    print(final_string)

