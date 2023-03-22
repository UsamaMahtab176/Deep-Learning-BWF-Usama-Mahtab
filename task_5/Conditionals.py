
# BWF - Usama Mahtab

# 5-1/5-2 Conditionals(If Statements)

car = 'Audi'
if car == 'Audi':
    print('My car is Audi')
if car.lower == 'audi':
    print('My car is audi!!')
if 3 + 5 == 8:
    print("3+5=8")
marks = 65
if marks >= 60:
    print("You have Passed")
if marks < 60:
    print("You have Failed!!")

cars = ['audi', 'mercedes', 'honda', 'porsche']
if 'porsche' in cars:
    print('I love expensive cars!')
if 'hayabusa' not in cars:
    print("Above is list of just cars")


# 5-3/5-4 Alien Colors
alien_color = input('What is color of alien? Green/Yellow/Red')
if alien_color.lower() == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points for shooting the alien!")

# 5-5 Alien Colors #3
alien_color = input("What is color of alien? Green/Yellow/Red")
if alien_color.lower() == 'green':
    print("You just earned 5 points for shooting the alien!")
elif alien_color.lower() == 'yellow':
    print("You just earned 10 points for shooting the alien!")
elif alien_color.lower() == 'red':
    print("You just earned 15 points for shooting the alien!")
else:
    print("Input Invalid")


# 5-6 Stages of life
age = int(input("Enter your age!"))
if age < 2:
    print("Person is a baby")
elif 4 > age >= 2:
    print("Person is a toddler")
elif 13 > age >= 4:
    print("Person is a kid")
elif 20 > age >= 13:
    print("Person is teenager")
elif 60 > age >= 20:
    print("Person is adult")
elif age >= 60:
    print("Person is old")


# 5-7. Favorite Fruit
favourite_fruits = ['banana', 'apple', 'mango']

if 'banana' in favourite_fruits:
    print('You really like bananas')
elif 'strawberry' in favourite_fruits:
    print('you really like strawberry')
elif 'apple' in favourite_fruits:
    print('you really like apples')
elif 'pomegranate' in favourite_fruits:
    print('you really like pomegranate')
elif 'mango' in favourite_fruits:
    print('you really like mango')


# 5-8/5-9/5-10. Hello Admin/No Users/Checking Usernames
usernames = ['faizan123', 'saim542', 'admin', 'M.daniyal.786', 'usama.176']

if len(usernames) == 0:
    print("No Users of System.We need to find some users")

else:
    for user in usernames:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + user + '! Thank you for logging in again!')

new_users = ['saim542', 'hasnat.476', 'm.saeed', 'M.daniyal.786', 'usama.176']
for user in new_users:
    if user.lower() in usernames:
        print('Username already taken!!')
    else:
        print("Username is available")


# 5-11 Ordinal Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num ==1:
        print(str(num)+'st')
    elif num ==2:
        print(str(num)+'nd')
    elif num ==3:
        print(str(num)+'rd')
    else:
        print(str(num)+'th')
