
# BWF - Usama Mahtab

# 9-8 Privileges
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
        self.privileges = Privileges()


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges of Administrator:")

        for privilege in self.privileges:
            print("-" + privilege)


admin = Admin("Usama", "Mahtab", "Software Developer", "usama.mahtab@gmail.com")
admin.describe_user()

admin.privileges.show_privileges()

admin.privileges.privileges = ["Add Post", "Delete Post", "Ban User"]
admin.privileges.show_privileges()


