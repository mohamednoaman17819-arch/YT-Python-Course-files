#String Methods

# text = "Python Programming"
# print(text.upper()) #PYTHON PROGRAMMING
# print(text.lower()) #python programming
# print(text.capitalize()) #Python programming
# print(text.find("Pro")) #7
# print(text.replace("Python","HTML")) #HTML Programming
# print(len(text)) #18

# text = "Python"
# text[0]="s"
# print(text)

#String Formating

name = "Ahmed"
age=25

info1="Name : %s , Age : %d"%(name,age)
info2="Name : {0} , Age : {1}".format(name,age)
info3=f"Name : {name} , Age : {age}"

print(info1,info2,info3,sep="\n")