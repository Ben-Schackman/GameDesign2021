#Ben Schackman
#6/10/2021
#Create a list of at least 5 elements (or ask the user to give the Values)
#Create a menu similar to what we did for the Strings MEthods
#in each selection you will allow the user to:
#1 insert elements either appending or inserting
#2 delete an element either by value or by index
#3  find if something in the list
#4  Find the index where an element is in the list
#5 reverse the order of the array

print("*      SPORTS MENU       *") 
print("*    1.- soccer          *")
print("*    2.- basketball      *")
print("*    3 - football        *")
print("*    4.- baseball        *")
print("*    5.- lacrosse        *")
print("*    6.- volleyball      *")
print("*    7.- Exit list       *")
print("**************************")

MySports=["Soccer", "basketball", "Football", "baseball", "Lacrosse"]
print(MySports)
MySports.append("volleyball")
for sport in MySports:
    print(sport, end= ",") 
    print()

for x in range (0,5):
    print(MySports[x], end= ",")
print(MySports[5])
MySports[1]="Football"
print (MySports[1:5])
if "soccer" in MySports:
        print("i got soccer")
else:
    print ("i want to play Lacrosse")
    Counter=len(MySports)


n=int(input("which sport"))

if "FIND" in x:
    print("what do you want to find")
    Var=input()
    indx=MySports.index(Var)
    print("index of ",Var," is ", indx)

