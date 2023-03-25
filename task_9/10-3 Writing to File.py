
# BWF - Usama Mahtab

# 10-3 Guest
name = input("Enter your name:")

file = 'guest.txt'
with open(file, 'w') as file_object:
    file_object.write("\n-"+name.title()+"\n")


# 10-4 Guest Book
active = True
while active:
    name = input("Enter you name:")
    print(f"Hi, {name} , You have been added to Guest List.... ")
    with open(file, 'a') as file_object:
        file_object.write("\n-"+name.title()+"\n")

    choice = input("Enter 'q' to quit OR any Key to Continue!!!!")
    if choice.lower() == 'q':
        active = False
