#Sets => Unique , Unindexable
# my_set = {1,2,3}
# print(my_set)

# set_a = set([1,2,3])
# set_b = set((1,2,3))
# print(set_a , set_b)

# empty_set=set()
# print(type(empty_set))

# valid_set = {5 , "hi" , (8,9)}
# print(valid_set)
# invalid_set = {5 , "hi" , [8,9]}
# print(invalid_set)

my_set = {1,2,3}
# my_set.add(4)
# my_set.update({4,5,6})
# my_set.remove(2)
# my_set.discard(4)

# a = my_set.pop()
# print("poped : ",a)

# my_set.clear()
# del my_set
# print(my_set)

# Union

# set_a = {1,2,3}
# set_b = {3,4,5}

# union_set = set_a.union(set_b)
# union_set = set_a | set_b
# print(union_set)

#Intersection

# set_a = {1,2,3}
# set_b = {3,4,5}

# inter_set = set_a.intersection(set_b)
# inter_set = set_a & set_b
# print(inter_set)

# Difference

# set_a = {1,2,3}
# set_b = {3,4,5}

# dif_set1 = set_a.difference(set_b)
# dif_set2 = set_b.difference(set_a)
# print(dif_set1 , dif_set2)


# Symmetric Difference

# set_a = {1,2,3}
# set_b = {3,4,5}

# sym_dif_set = set_a.symmetric_difference(set_b)
# sym_dif_set = set_a ^ set_b
# print(sym_dif_set)