
# Usama Mahtab - BWF

# 3-1 Names

names = ['Daniyal', 'Uzair', 'Usama', 'Hasnat']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3-2 Greetings

print("Hi "+names[0]+"! How are you?")
print("Hi "+names[1]+"! How are you?")
print("Hi "+names[2]+"! How are you?")
print("Hi "+names[3]+"! How are you?")

# 3-3 Your Own List

list = ['motorcycle','car','watch']
print('I would like to own Honda '+list[0])
print('I would like to own Mercedes '+list[1])
print('I would like to own Rolex '+list[2])

#  3-4 Guest List

guest = ['Isac Newton', 'Noam Chomsky', 'Nikola Tesla']
print('Hi '+guest[0]+ '! I would like to invite you to dinner in my house')
print('Hi '+guest[1]+ '! I would like to invite you to dinner in my house')
print('Hi '+guest[2]+ '! I would like to invite you to dinner in my house')

# 3-5 Changing Guest List

print(guest[0]+ ' cannot make it to dinner!')
guest[0] = 'Thomas Edison'
print('Hi '+guest[0]+ '! I would like to invite you to dinner in my house')
print('Hi '+guest[1]+ '! I would like to invite you to dinner in my house')
print('Hi '+guest[2]+ '! I would like to invite you to dinner in my house')

#  3-6 More Guests

print("I've found a bigger Dinner table!!")
guest.insert(0,'Che Guevara')
guest.insert(2, 'Abu Nasr Al-Farabi')
guest.append('Al-Ghazali')
print('Hi '+guest[0]+ '! I would like to invite you to dinner in my house')
print('Hi '+guest[1]+ '! I would like to invite you to dinner in my house')
print('Hi '+guest[2]+ '! I would like to invite you to dinner in my house')
print('Hi '+guest[3]+ '! I would like to invite you to dinner in my house')
print('Hi '+guest[4]+ '! I would like to invite you to dinner in my house')
print('Hi '+guest[5]+ '! I would like to invite you to dinner in my house')

# 3-7 Shrinking the list

print("Jeez! I have just found out that I can invite only two people!!")
while len(guest)>2:
    print('Hi ' + guest[0] + '! Sorry I cannot invite you to dinner!')
    guest.pop(0)
print('Hi '+guest[0]+ '! I would like to invite you to dinner in my house')
print('Hi '+guest[1]+ '! I would like to invite you to dinner in my house')
del guest[0]
del guest[1]
print(guest)

# 3-8 Seeing the world

locations = ['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']

print("Original order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)

# 3-9. Dinner Guests

guest = ['Isac Newton', 'Noam Chomsky', 'Nikola Tesla']
length = len(guest)
print('I would invite '+length+' people to the dinner')

