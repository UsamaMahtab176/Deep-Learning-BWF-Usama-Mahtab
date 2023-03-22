
# BWF-Usama Mahtab

# timeit (timing your code)
import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"
# code 1 snippet whose execution time is to be measured
mycode1 = '''
def example():
    mylist = []
    for x in range(100):
        mylist.append(sqrt(x))
'''
# timeit statement for code 1 snippet
print("Running time for first code snippet")
print(timeit.timeit(setup=mysetup, stmt=mycode1, number=1000000))
# code 2 snippet whose execution time is to be measured
mycode2 = '''
def example():
    mylist = list()
    for x in range(100):
        mylist.append(sqrt(x))
'''
# timeit statement for code 2 snippet
print("Running time for second code snippet")
print(timeit.timeit(setup=mysetup, stmt=mycode2, number=1000000))
