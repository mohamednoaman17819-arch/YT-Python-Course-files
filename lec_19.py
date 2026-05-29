# Dictionary

# "key" : "value"

# person = {
#     "name" : "Ahmed",
#     "age" : 30

# }

# person = dict(name = "ahmed" , age = 30)

# person = dict([("name","ahmed"),("age",30)])
# print(person)

# empty_dict = dict()
# empty_dict2 = {}

# print(type(empty_dict) , type(empty_dict2))

# valid_dict = {
#     "name" : "ahmed",
#     10 : "int",
#     (1,2) : "tuple"
# }
# print(valid_dict)

# invalid_dict = {
#     "name" : "ahmed",
#     10 : "int",
#     [1,2] : "list"
# }
# print(invalid_dict)


person = {
    "name" : "Ahmed",
    "age" : 30
}

# print(person["salary"])
# print(person.get("salary" , " not found"))

#add

# person["salary"] = 50000
person["age"] = 35

del person["age"]

# del_value = person.popitem()
del_value = person.pop("salary" , "not found")

print(person)
print(del_value)