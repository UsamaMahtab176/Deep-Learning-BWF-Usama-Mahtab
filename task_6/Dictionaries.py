
# BWF - Usama Mahtab

# 6-1 Person
personal_info = {'first-name': 'Zaryab', 'last-name': 'Shahzad', 'Age': '21', 'city': 'Rawalpindi'}

print(personal_info.keys(), personal_info.values())

print(personal_info['first-name'])
print(personal_info['last-name'])
print(personal_info['Age'])
print(personal_info['city'])

# 6-2 Favorite Numbers
favorite_number = {}
active = True
while active:
    name = input("Enter you name: \n")
    fav_num = int(input('Enter your favourite number:\n'))
    favorite_number[name] = fav_num

    choice = input("Press 'q' to QUIT else press any key:\n")
    if choice.lower() == 'q':
        active = False
print(favorite_number)

# 6-3/6-4 Glossary
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
}

# printing without loop
print("String :" + glossary['string'])
print("Comment :" + glossary['comment'])
print("List :" + glossary['list'])
print("Loop :" + glossary['string'])
print("Dictionary :" + glossary['dictionary'])

# printing with loop
for word, info in glossary.items():
    print(word + ":" + info)

# 6-5 Rivers
rivers = {'nile': 'Egypt', 'indus': 'Pakistan', 'amazon': 'Brazil'}

for river, country in rivers.items():
    print("The " + river.title() + ' runs in ' + country.title())

print("\nThe following rivers are included in this data set:")
for keys in rivers.keys():
    print(keys)
print("\nThe following countries are included in this data set:")
for values in rivers.values():
    print(values)

# 6-6 Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
programmers = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']

for prog in programmers:
    if prog in favorite_languages.keys():
        print("Thanks! " + prog.title() + " for taking the poll")
    else:
        print(prog.title() + ", Whats your favourite programming language?")

# 6-7 People
personal_info_1 = {'first-name': 'Zaryab', 'last-name': 'Shahzad', 'Age': '22', 'city': 'Rawalpindi'}
personal_info_2 = {'first-name': 'Uzair', 'last-name': 'Asim', 'Age': '21', 'city': 'Islamabad'}
personal_info_3 = {'first-name': 'Usama', 'last-name': 'Saeed', 'Age': '23', 'city': 'Haripur'}

people = [personal_info_1, personal_info_2, personal_info_3]

for p in people:
    print(p)

# 6-8 Pets
pet_1 = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pet_2 = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pet_3 = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets = [pet_1, pet_2, pet_3]

print("Information of pets:\n")
for pet in pets:
    print("Name: " + pet['name'])
    print("Animal_Type: " + pet['animal type'])
    print("Owner: " + pet["owner"])
    print("Weight: " + str(pet["weight"]))
    print("Eats: " + pet["eats"])
    print("\n")

# 6-9 Favourite Places
favorite_places = {
    'Zaryab': ['bear mountain', 'death valley', 'tierra del fuego'],
    'Uzair': ['hawaii', 'iceland'],
    'Usama': ['mt. verstovia', 'the playground', 'south carolina']
}

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())

# 6-10 Favourite numbers
favorite_numbers = {
    'Usama': [42, 17],
    'Waleed': [42, 39, 56],
    'Hasnat': [7, 12],
}

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))

# 6-11 Cities

cities = {'Islamabad': {
    'country': 'Pakistan', 'population': 1015000, 'fact': 'Islamabad is the capital of Pakistan.'
    },
    'New Delhi': {
    'country': 'India' , 'population': 31181000, 'fact': 'New Delhi is the capital of India.'
    },
    'Dhaka': {
    'country':'Bangladesh', "population": 25359144 , 'fact': 'Dhaka is the capital of Bangladesh.'
    }
    }
for city, info in cities.items():
    print('\n')
    print("Information about " + city+":\n")
    print("Country: " + info['country'])
    print("Population: " + str(info['population']))
    print("Fact: " + info['fact'])



