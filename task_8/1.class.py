
# BWF - Usama Mahtab

# 9-1 Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is open for Service")

    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant_name}")
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine")


restaurant = Restaurant("Asian Wok", "Chinese")
print(restaurant.restaurant_name, restaurant.cuisine_type)

restaurant.open_restaurant()
restaurant.describe_restaurant()

# 9-2 Three restaurants
restaurant_1 = Restaurant("Ginyaki", "Japanese")
restaurant_2 = Restaurant("Al_Beirut Lebanese Cuisine", "Lebanese Arab")
restaurant_3 = Restaurant("Tuscany Courtyard", "Italian")

print("\n")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()


# 9-3 Users
class User:
    def __init__(self, first_name, last_name, occupation, email):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.email = email

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Occupation: {self.occupation}")
        print(f"E-mail: {self.email}")

    def greet_user(self):
        print(f"\nHello {self.first_name}!\n How's your day going?")


user_1 = User("Usama", "Mahtab", "Software Developer", "usama.mahtab1@gmail.com")
user_2 = User("Zaryab", "Shahzad", "Businessman", "zaryab12@gmail.com")
user_3 = User("Abtuha", "Nisar", "Banker", "abtuha.nisar@gmail.com")

user_1.greet_user()
user_1.describe_user()
user_2.greet_user()
user_2.describe_user()
user_3.greet_user()
user_3.describe_user()
