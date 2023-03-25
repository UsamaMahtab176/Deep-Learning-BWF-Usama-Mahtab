
# BWF - Usama Mahtab

# 9-6 Ice-Cream Stand
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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice-Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = []

    def show_flavours(self):
        print("\nFollowing flavours are available:")
        for flavour in self.flavours:
            print("\n- "+flavour.title())


iceCream_stand = IceCreamStand("Baskin Robin's")
iceCream_stand.flavours = ["vanilla", "mango", "straw-berry", "black-berry"]
iceCream_stand.show_flavours()


# 9-7 Admin
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


class Admin(User):
    def __init__(self, first_name, last_name, occupation, email):
        super().__init__(first_name, last_name, occupation, email)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivileges of Administrator:")

        for prvilege in self.privileges:
            print("-"+prvilege)


print("\n")
admin = Admin("Usama", "Mahtab", "Software Developer", "usama.mahtab@gmail.com")
admin.describe_user()

admin.privileges = ["Add Post", "Delete Post", "Ban User"]
admin.show_privileges()


