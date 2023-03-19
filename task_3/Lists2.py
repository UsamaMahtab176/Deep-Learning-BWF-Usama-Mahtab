
# Usama Mahtab - BWF

# 4-1 Pizza

pizza = ['papperoni pizza', 'BBQ Chicken pizza', 'Margherita pizza']

for i in range(len(pizza)):
    print('I like ' + pizza[i] + ' pizza')

print("I love pizza so much that i can eat it in all 3 meals of a day!!")

# 4-2 Animals

animals = ['cat', 'dog', 'parrot']
for animal in animals:
    print(animal + " would make a great pet")
print("Any of these animals would be a great pet")

# 4-3 Counting to twenty

for i in range(20):
    print(i + 1)

# 4-4 One Million

million = [value for value in range(1, 100000)]
print(million)

# 4-5 Summing a million
print('Minimum:')
print(min(million))
print("Maximum:")
print(max(million))
sum = 0
for i in range(len(million)):
    sum = sum + million[i]
print(sum)

# 4-6 Odd numbers

Odd = [value for value in range(1, 20, 2)]
print("ODD NUMBERS!!!!")
for i in Odd:
    print(i)

# 4-7 Threes

Threes = [value for value in range(3, 31, 3)]
print("Multiples of 3:")
for i in Threes:
    print(i)

# 4-8/4-9 Cubes

cube = [value ** 3 for value in range(1, 11, 1)]
print("printing first 10 cubes:")
for i in cube:
    print(i)

# 4-10 Slices

pizza_flavors = ['pepperoni', 'mushroom', 'cheese', 'vegetarian', 'meat lovers', 'hawaiian', 'barbecue chicken', 'garlic chicken']
print("The first three items in the list are:")
print(pizza_flavors[:3])

print("Three items from the middle of the list are:")
middle_start = len(pizza_flavors)//2 - 1
middle_end = middle_start + 3
print(pizza_flavors[middle_start:middle_end])

print("The last three items in the list are:")
print(pizza_flavors[-3:])

# 4-11 My Pizza, Your Pizza

pizzas = ['pepperoni', 'mushroom', 'sausage']
friend_pizzas = pizzas.copy()
pizzas.append('cheese')
friend_pizzas.append('vegetarian')
print("My favorite pizzas are:")
for pizza in pizzas:
    print("- " + pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)

# 4-12 More Loops

foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = ['pizza', 'cannoli', 'ice cream']

print("My favourite foods are:")
for food in foods:
    print(food)

print("My Friend's Favourite food is:")
for food in friend_foods:
    print(food)


