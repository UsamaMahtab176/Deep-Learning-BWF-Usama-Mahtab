
# BWF - Usama Mahtab


# 8-3 T-Shirt
def t_shirt(size, message):
    print("The size of shirt will be:" + size.title())
    print("The message to be printed on shirt will be:\n" + '"' + message + '"')


t_shirt("Large", "Muslim,24/7,365")
t_shirt(size='Medium', message='Maulvi with an attitude')


# 8-4 Large Shirts
def t_shirt(size='Large', message='I love python'):
    print("The size of shirt will be:" + size.title())
    print("The message to be printed on shirt will be:\n" + '"' + message.title() + '"')


t_shirt('large')
t_shirt('medium')
t_shirt("Small", "Python is better than any other programming language")


# 8-5 Cities
def describe_city(name, country='Pakistan'):
    print(name.title() + " is in " + country.title())


describe_city("Islamabad")
describe_city("Ohio", "USA")


