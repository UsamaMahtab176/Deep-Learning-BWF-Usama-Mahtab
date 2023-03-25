
# BWF - Usama Mahtab

# 9-4 Number Served
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is open for Service")

    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant_name}")
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine")

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self, additional):
        self.number_served += additional


restaurant = Restaurant("Al_Beirut Lebanese Cuisine", "Lebanese Arab")
restaurant.number_served = 457

restaurant.set_number_served(678)
print(f"Customer Served: {restaurant.number_served}")
restaurant.increment_number_served(200)
print(f"Customer Served: {restaurant.number_served}")


# 9-5 Login Attempts
class User:
    def __init__(self, first_name, last_name, occupation, email):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Occupation: {self.occupation}")
        print(f"E-mail: {self.email}")

    def greet_user(self):
        print(f"\nHello {self.first_name}!\n How's your day going?")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("Uzair", "Asim", "Web Developer", "uzair.asim@gmail.com")

print("\nIncrementing Login Attempts:")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)

print("\nResetting Login Attempts")
user.reset_login_attempts()
print(user.login_attempts)
