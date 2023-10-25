#Assignment 6.1

file_input = input("Enter the file name: ")
try:
    fhand = open(file_input)
except:
    print("The file can not be opened: ", file_input)
else:
    for line in fhand:
        line = line.upper().rstrip()
        print(line)
    
#Assignment 6.2
fhand2 = open("mbox.txt","r")
count = 0
for lines in fhand2:
    if lines.startswith("From: "):
        lines = lines.rstrip()
        atpos = lines.find("@")
        host = lines[atpos+1:]
        count += 1
        print(host)
print(f"Total {count} hosts printed")

#Assignment 6.3
file_name2 = input("Enter the file name: ")
total = 0
count2 = 0
try:
    fhand3 = open(file_name2,"r")
except:
    print("File can not be opened: ",file_name2)
else:
    lines2 = fhand3.readlines()
    for line in lines2:
        if line.startswith("X-DSPAM-Confidence:"):
            separation = line.split(":")
            if len(separation) == 2:
                number = float(separation[1])
                total += number
                count2+=1
    print("Avarage Spam Confidence: ", (total/count2))





