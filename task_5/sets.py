
# BWF - Usama Mahtab

# Set and Intersection between two or more sets
A = {5, 6, 8, 12, 14, 15}
B = {2, 4, 6, 10, 15, 18}
C = {1, 4, 8, 15, 18, 21}

common = A.intersection(B)
print(common)
common = common.intersection(C)
print(common)

# Different Operation on sets
A = {5, 6, 8, 12, 14, 15}
B = {2, 4, 6, 10, 15, 18}

# union of sets
print("Union of A and B is \n")
print(A.union(B))
# intersection of sets
print("Intersection of A and B is \n")
print(A.intersection(B))
# difference of sets
print("Difference of A and B is \n")
print(A.difference(B))
# symmetric difference of sets
print("Symmetric Difference of A and B is \n")
print(A.symmetric_difference(B))


