
# BWF - Usama Mahtab

# 10-5  Programming Poll
file = "programming_poll.txt"

with open(file, 'w') as file_object:
    file_object.write("Reasons to like Programming \n")

active = True
while active:
    reason = input("Enter reason ehy you like programming:\n")
    with open(file, 'a') as file_object:
        file_object.write('\n- '+reason+' \n')

    choice = input("Enter 'x' to exit else enter any key to continue..!!\n")
    if choice.lower() == 'x':
        active = False
