
# BWF - Usama Mahtab

# Enumerate() Function

cars = ['audi', 'mercedes', 'honda', 'porsche']

# Enumerarte object
obj1 = enumerate(cars)
print(type(obj1))
print(list(obj1))

char = "geek"
obj2 = enumerate(char)
print(type(obj2))
print(list(obj2))

# Enumerate() function in loops

cars = ['audi', 'mercedes', 'honda', 'porsche']

for car in enumerate(cars):
    print(car)
for count, car in enumerate(cars, 100):
    print(count, car)
