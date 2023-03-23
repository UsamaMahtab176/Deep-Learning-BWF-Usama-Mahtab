
# BWF - Usama Mahtab

# 8-9 Magicians
def show_magicians(magicians):
    for magician in magicians:
        print(magician)


magicians = ['David Blaine', 'David Copperfield', 'Apollo Robbins', 'Shin Lim']

show_magicians(magicians)


# 8-10/8-11  Great Magicians
def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians


magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)

magicians = ['David Blaine', 'David Copperfield', 'Apollo Robbins', 'Shin Lim']
great_magicians = make_great(magicians[:])
print('\n')
print('Great Magicians:')
show_magicians(great_magicians)
print('\n')
print('Original List:')
show_magicians(magicians)

