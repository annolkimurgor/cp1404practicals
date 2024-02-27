

name= input("Enter your name: ")
with open("name.txt", 'w') as file:
    file.write(name)

with open("name.txt", 'r') as file:
        name = file.read()
        print("Your name is", name)

with open(nmbers.txt)
