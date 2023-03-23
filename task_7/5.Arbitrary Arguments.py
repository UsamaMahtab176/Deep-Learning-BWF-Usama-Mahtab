
# BWF - Usama Mahtab

# 8-12 Sandwiches
def make_sandwich(*ingredients):
    print("Your sandwich contains:\n")
    for ingredient in ingredients:
        print(ingredient)
    print('\n')


make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')


# 8-13 User Profile
def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
user_profile = build_profile("isac", 'mewton', location='kensignton', field='physics', nationality='British')
print(user_profile)
user_profile = build_profile("Nikola", "Tesla", loacation="Smiljan,Croatia", field="Physics")
print(user_profile)


# 8-14 Cars
def make_car(manufacturer, model, **car_info):
    car = {'Manufacturer': manufacturer, 'Model': model}
    for key,info in car_info.items():
        car[key] = info
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
