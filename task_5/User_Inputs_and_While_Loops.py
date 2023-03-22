
# BWF - Usama Mahtab

#  7-1  Rental Car
car = input("What type of car you want?")
print("Let me see If I can find you a " + car)


#  7-2 Restaurant Seating
people = int(input("How many people are in dinner group?"))

if people > 8:
    print("You'll have to wait for the Table")
else:
    print("Your Dinner table is ready")


#  7-3 Multiples of Ten
num = int(input("Enter any integer!\n"))

if num % 10 == 0:
    print("Given number is multiple of 10")
else:
    print("Given number is not a multiple of 10")


# 7-4 Pizza Toppings
Topping = input("Enter you favourite pizza topping\n")
while Topping.lower() != 'quit':
    print(Topping+" will be added to your pizza as a topping")
    Topping = input("Enter you favourite pizza topping\n")


# 7-5/7-6 Movie Tickets/Three Exits
active = True
while active:
    age = int(input("Enter age:\n"))
    if age < 3:
        print("You ticket is free!")
    elif 3 <= age < 12:
        print("Your ticket price is 10$")
    elif age>=12:
        print("Your ticket price is 15$")

    choice = input("Do you want to continue?\n")
    if choice.lower() == 'no':
        active = False

# 7-7 Infinite Loop
while True:
    print("This is an INFINITE loop")