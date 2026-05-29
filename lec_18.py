# Subset

# set_a={1,2,3}
# set_b={1,2,3,4}
# print(set_a.issubset(set_b))
# print(set_a < set_b)

# Superset

# set_a={1,2,3}
# set_b={1,2,3,4}
# print(set_b.issuperset(set_a))
# print(set_b > set_a)

# proper superset / proper subset

# set_a={1,2,3}
# set_b={1,2,3,4,5}

# print(set_a < set_b)
# print(set_b > set_a)

#disjoint
# set_a={1,2,3}
# set_b={4,5}
# print(set_a.isdisjoint(set_b))

# my_set = {"A","B","C"}
# for char in my_set:
#     print(char)

# Frozenset
# frozen = frozenset([1,2,3,4])
# frozen.add(5)
# print(frozen)

frozen_a = frozenset([1,2,3])
frozen_b = frozenset([2,3,4])

print(frozen_a | frozen_b) #union
print(frozen_a & frozen_b) #intersection
print(frozen_a - frozen_b) #difference
