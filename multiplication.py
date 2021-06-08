# Ben Schackman
#6/4/2021 
# We are going to print multiplication tables
# using print statement and variable
# input ---> variable is a container that will hold data and an adress is assigned 
# variables need to have a valid name
#use the function input ()
base = int(input())
print(type(base))
print("multiplication Table", base)

for counter2 in range (1,11): 
    print(base, "x", counter2, "=", counter2 * base)
