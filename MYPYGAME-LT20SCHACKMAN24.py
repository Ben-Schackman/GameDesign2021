#Mateo Lanzillotta
#learn how to change colors
#Learn how to draw shapes
#Learn how to control objects on the screen with key
from pygame.cursors import arrow
 
#K_UP                up arrow
 
import time, sys, pygame, os
os.system('cls')
pygame.init() #initialize the game
purple=[200,0,200]
white=[255,255,255]
red=[200,25,0]
green=[0,200,50]
WIDTH=500
HEIGHT=600
 
screen=pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(green)
pygame.time.delay(100)
pygame.display.set_caption("Mateo's Game")
x=10
y=10
wbox=20
hbox=20
rect1=pygame.Rect(x,y,wbox,hbox)
pygame.draw.rect(screen, red, rect1)
speed=2
 
check = True
while check:                    # ALL YOUR PROGRAMS WITH PYGAME MUST HAVE THIS PART
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            check = False
    
    KB=pygame.key.get_pressed()  #Checking is a key has been pressed
    if KB[pygame.K_RIGHT]:
        rect1.x +=speed #move rectangle two pixels to the right
    if KB[pygame.K_LEFT]:
        rect1.x -=speed #move rectangle two pixels to the left
    screen.fill(green)
    pygame.draw.rect(screen, red, rect1)
    pygame.display.update()
    pygame.time.delay(30)
print("Goodbye")
pygame.time.delay(100) #delay in milliseconds
 
pygame.quit()
