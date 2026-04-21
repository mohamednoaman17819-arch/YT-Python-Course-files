# Template String
from string import Template

temp = Template("Hello $name , You are $age years old")
message = temp.substitute(name="mohamed" , age=25)
print(message)

#**************
name = "mohamed"
age= "25"

temp=t"Hello {name} , You are {age} years old"
print(temp.strings) #('Hello ', ' , You are ', ' years old .')
print(temp.interpolations) #("value", "expression", "conversion", "format_spec")
print(temp.values) #('mohamed', '25')
 



def built_template(t):
    values=[]
    for i in t:
        if isinstance (i,str):
            values.append(i)
        else:
            values.append(i.value)
    return " ".join(values)

print(built_template(temp))