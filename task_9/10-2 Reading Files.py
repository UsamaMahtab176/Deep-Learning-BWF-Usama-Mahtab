
# BWF - Usama Mahtab

# 10-2 Learning C
filename = 'learning_python.txt'

with open(filename) as file_object:
    print("\n")
    print("Contents before Replace method!!!")
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    print("\n")
    print("Contents after Replace method")
    for line in file_object:
        print(line.replace('python', 'C++').rstrip())
