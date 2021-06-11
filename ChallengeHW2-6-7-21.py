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
print("*       My game          *")
print("*         Menu           *")
print("*    1.- level1          *")
print("*    2.- level2          *")
print("*    3 - level3          *")
print("*    4.- level4          *")
print("*    5.- level5          *")
print("*    6.- Print scores    *")
print("*    7.- Exit Game       *")
print("**************************")
answer = int(input().strip())

while answer!=4:
    if answer == 1:
        print("welcome to level 1. (INSERT LEVEL HERE)".title())
    if answer == 2:
        print("welcome to level 2. (INSERT LEVEL HERE)".swapcase())
    if answer == 3:
        print("Highscore: Ben - 1500 pts")
        print("second: jadon - 1200")
        print("third: zander - 972")
        print("fourth: Thomas - 542")
        print("fifth: Mateo - 388")
        print("sixth: Brenna - -200")
        print("seventh: Payton - -457")
    if answer == 4:
        print("welcome to level 4. (INSERT LEVEL HERE)".
    print("**************************")
    print("*       My game          *")
    print("*         Menu           *")
    print("*    1.- level1          *")
    print("*    2.- level2          *")
    print("*    3 - level3          *")
    print("*    4.- level4          *")
    print("*    5.- level5          *")
    print("*    6.- Print scores    *")
    print("*    7.- Exit Game       *")
    print("**************************")
    answer = int(input())
    
print("GOODBYE HAVE A NICE DAY!".center(100))