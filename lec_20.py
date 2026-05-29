# person = {
#     "name" : "Ahmed",
#     "age" : 30
# }

# key = person.keys()
# print(key)

# print(person.values())
# print(person.items())

# person2 = person.copy()
# print(person2)
# #person["salary"] = 5000
# person.update({"salary":5000})
# print(person)

# keys = ["name" , "age"]
# unknown_dict = dict.fromkeys(keys , "Unknown")
# print(unknown_dict)

# people = {
#     "person1" :{
#         "name" : "Ahmed",
#         "age" : 30
#     },
#       "person2" :{
#         "name" : "mohamed",
#         "age" : 35
#     },
# }

# print(people["person1"]["age"])

# people["person2"]["city"] = "cairo"
# print(people["person2"]["city"])

# del people["person2"]["city"]
# print(people["person2"])

# person1 ={
#         "name" : "Ahmed",
#         "age" : 30
#     }

# for key in person1.keys():
#     print(key)

# for value in person1.values():
#     print(value)

# for key , value in person1.items():
#     print(f"{key} : {value}")



people = {
    "person1" :{
        "name" : "Ahmed",
        "age" : 30
    },
      "person2" :{
        "name" : "mohamed",
        "age" : 35
    },
}

for person , details in people.items():
    print(f"{person}")
    for key , value in details.items():
        print(f"{key} : {value}")