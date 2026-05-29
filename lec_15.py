# Mutable Objects
# ----------------
# Lists , Dictionaries , Sets
# Elements can be added, removed, or changed.
# Key-value pairs can be updated.
# New items can be added or existing ones removed.

# Immutable Objects
# -------------------
# Numbers: int, float, complex, bool.
# Strings: Any modification results in a new string.
# Tuples : Fixed sequences that cannot change after creation.
# Frozen Sets : Immutable version of a set.

# List
# fruits = ["apple","banana","cherry","fig"]
# print(fruits[0])
# print(fruits[0:2])
# print(fruits[::2])
# print(fruits[-1])

# 2D List

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]

# for i in matrix:
#     for j in i:
#         print(j , end=" ")

# list1=[1,2,3]
# list2=[4,5,6]

# total_list = list1+list2
# print(total_list)

# repeated_list = list1 * 2
# print(repeated_list)

# fruits = ["apple","banana","cherry","fig"]
# print("apple" in fruits)
# print("mango" in fruits)

list1=[1,2,3,4,5,6,7]

# print(len(list1))
# print(max(list1), min(list1))

# first , *second , third = list1
# print(first , second , third)

# list1.append(10)
# list1.remove(5)
# list1.pop(4)
list1.clear()
print(list1)

