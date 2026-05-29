# While Loop

# while condition:
#   code

# count = 5

# while count > 0:
#     print(count)
#     count -=1
# print(count)

# text="Python"

# reversed_text="" 
# index = len(text) -1
# while index>=0:
#     reversed_text += text[index]
#     index -=1
# print("Reversed text :",reversed_text)

password = "12345"
print("Enter Password : ")
entered_password = input()
while password != entered_password:
    entered_password = input("password is wrong \n")
print("Password accepted")


