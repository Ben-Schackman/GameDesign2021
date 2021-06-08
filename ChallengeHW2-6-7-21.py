#Ben Schackman
# 6/7/2021
#  write a program that  prints a menu
# **************************
# *       My game              *
# *         Menu                  *
# *                                    *
# *    1.- level1                 *
# *    2.- level2                 *
# *    3.- Print scores        *
# *    4.- Exit Game          *
# **************************

# ask user for choice
# while answer is not 4:
#      blah blah
#      Menu
#      answer


# Print good bye

print("**************************")
print("*       My game          *")
print("*         Menu           *")
print("*                        *")
print("*    1.- level1          *")
print("*    2.- level2          *")
print("*    3.- Print scores    *")
print("*    4.- Exit Game       *")
print("**************************")
answer = int(input())

while answer!=4:
    if answer == 1:
        print("welcome to level 1. (INSERT LEVEL HERE)")
    if answer == 2:
        print("welcome to level 2. (INSERT LEVEL HERE)")
    if answer == 3:
        print("Highscore: Ben - 1500 pts")
        print("second: jadon")
        print("third: zander")
        print("fourth: Thomas")
        print("fifth: Mateo")
        print("sixth: Brenna")
    print("**************************")
    print("*       My game          *")
    print("*         Menu           *")
    print("*                        *")
    print("*    1.- level1          *")
    print("*    2.- level2          *")
    print("*    3.- Print scores    *")
    print("*    4.- Exit Game       *")
    print("**************************")
    answer = int(input())
print("GOOD JOB")