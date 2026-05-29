
l1 = [[1,2,3],[4,5,6],[7,8,9]]
print(id(l1))               #2066108939008
print(id(l1[0]))            #2066107487040

#Both variables point to the same object in memory.
l2 = l1
print(id(l2))               #2066108939008
print(id(l2[0]))            #2066107487040

#This creates a new outer list only.
l3 = l1.copy()
print(id(l3))               #2066107486336
print(id(l3[0]))            #2066107487040


import copy

l1 = [[1,2,3],[4,5,6],[7,8,9]]
print(id(l1))                   #2469493130880
print(id(l1[0]))                #2469493299328

shallow = copy.copy(l1)
print(id(shallow))              #2469493130944
print(id(shallow[0]))           #2469493299328

deep = copy.deepcopy(l1)
print(id(deep))                 #2469493136768      
print(id(deep[0]))              #2469493132096


# == & is

l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 =l1.copy()

print(l1 == l2)         #True
print(l1 is l2)         #False


