#ben schackman
#06/14/2021
#game w/ menu
import os
import sys 
import time
import random
import datetime

os.system('cls')

print("1.- play the game \n2.- Print top scores(print the score file)\n3.  Exit")
selection = int(input().strip())
while selection!=3:
    if selection == 1:
        gameWords= ['Jump','Swim','Skateboard','computer','keyboard','Triangle','laptop','Square','charger','mouse','software','rectangle']
        name =input("What is your name?")
        print(name, end = " ")
        answer = input(" Do you want to play? ").upper()
        #yes -> YES
        print("\n ",gameWords) #delete when code works properly 
        while "Y" in answer:
            print(name," Good luck")
            word=random.choice(gameWords) #stores word to be guessed
            print(word)
            turns =10  # defines turns
            guesses=''
            counter=len(word)
            wrongGuesses= 0
            while turns >0 and counter>=0:
                for char in word: #graphic of guesses
                    if char in guesses:
                        print(char, end=' ')
                    else:
                        print('_', end=' ')
                newGuess=input("\n Give me a letter ") #input
                if newGuess in word:
                    ball= word.count(newGuess)
                    counter= counter - ball
                    guesses += newGuess    #guesses= guesses+newGuesses
                    print("You are Right!!" )
                
                else:
                    turns -= 1
                    print ("Sorry that is wrong you still have ", turns," turns") 
                    wrongGuesses = wrongGuesses + 1
            if turns > 0: #if they win - add them to leader board file
                hsFile = open('hs.txt','a')
                hsFile.write("Name: ")
                hsFile.write(name)
                hsFile.write("Wrong Guesses: ")
                hsFile.close
        
            answer = input(" Do you want to play? ").upper()
            def printscore():
                def updatescore():
                    print(name,"you score is: ", score)
            selection = 4
        
    if selection == 2:
        hsFile = open('hs.txt', 'r')
        print(hsFile.read())
        hsFile.close
    print("1.- play the game \n2.- Print top scores(print the score file)\n 3.  Exit")
    selection = int(input().strip())




# print("hello... let me guess your name...")
# time.sleep(2) #basically a wait function - creates a pause in the program
# print("...almost...")
# print("... yes, you are Ben")
# time.sleep(2)
# os.system('cls') #clears console
# file=input("Please add file name add extension of the file. Ex File.txt :")
# #check if the file exists
# if os.path.exists(file):
#     f1= open('txtTest.txt','r' )
#     print(f1.read())
#     f1.close
# else:
#     print("the file does not exist")
