#Tuples

# fruits = ("apple","banana","cherry")

# print(fruits[0])
# print(fruits[0:2])
# print(fruits[::2])
# print(fruits[-1])

# tuple1 = (1,2,3)
# tuple2 = (4,5,6)
# total_tuple= tuple1 + tuple2
# print(total_tuple)
# repeated_tuple = tuple1 *2
# print(repeated_tuple)

# fruits = ("apple","banana","cherry")
# print("apple" in fruits)
# print("mango" not in fruits)

tuple2 = (4,5,6,7,8,9)

# print(len(tuple2))
# print(max(tuple2) , min(tuple2))

x,*y,z = tuple2
print(x,y,z)