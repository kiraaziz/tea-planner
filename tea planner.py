print ("----------WELCOM TO TEA PLANNER----------")
name = input("what is the name of the project ")
table = [0]*int(input("how many option in the planner "))
option_name= [0]*len(table)
size = int(input("choose the volume of every option "))


for x in range (len(table)):
    option_name [x] = input("--option name ")
    
    table [x] = int(input("--volume "))
    for y in range (2):
        print("-")

max_name = option_name[0]
for x in range (len(table)):
    if len(option_name[x]) > len(max_name) :
        max_name = option_name[x]
Nmax = len(max_name)


print("----------"+name+"----------")
print("")
print("")


for x in range (len(table)):
    print(option_name[x],end="")
    espace = Nmax - len(option_name[x])
    for f in range (espace + 2):
        print(" ",end="")
    for y in range (table[x]):
        for k in range (size):
            print("-",end="")
    print("")
    print("")
