with open("students.txt", "r") as file:
    for line in file:
        print (line.strip())


with open("students.txt", "r") as file:
     for line in file:
          print(line[1])


with open("students.txt", "r") as file:
     for line in file:
          if len > 6: 
            print


new-line = input("Enter a name to add to the list")
with open("students.txt", "a") as file:
    file.write(new-line + "/n")