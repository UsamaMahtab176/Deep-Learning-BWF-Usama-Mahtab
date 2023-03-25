
# BWF - Usama Mahtab

# 10-1 Learning Python
filename = 'learning_python.txt'

"""Reading File as a whole"""
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

"""Reading File using a Loop"""
with open(filename) as file_object:
    for line in file_object:
        print(line)

"""Reading File as a List"""
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

