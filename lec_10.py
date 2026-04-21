#If Statement

# if condition :
#     excute 

# if (5>3):
#     print("5 is greater than 3")
# else:
#     print(" there is something wrong!")

# score = int(input("Enter your score"))

# if score >= 90:
#     print("A")
# elif score >=80:
#     print("B")
# elif score>=70:
#     print("C")
# else:
#     print("D")

# age = 15
# has_license=True

# if age>=18:
#     if has_license:
#         print("You can drive")
#     else:
#         print("you can get a license")

# else:
#     print("you are not old enough to drive")

# >16 or supervised
# age =25
# is_supervised=True

# if age >= 18 and is_supervised:
#     print("you can watch the movie")
# else:
#     print("you can't watch the movie")

# more 16 and less than 50
# age=25
# if 16<age<50:
#     print("You can watch the movie")

age=20
# if age<16:
#     print("Minor")
# else:
#     print("adult")
status = "adult" if age>=16 else "minor"
print(status)