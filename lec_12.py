n = 7

for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print("* ",end="")
    print()


text="python"
l=[1,2,3,4]
l.reverse()
print(l)