# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
win = pygame.display.set_mode([500, 480])
pygame.display.set_caption("First Game")

#adding sprites
walkRight = [pygame.image.load('resources/R1.png'), pygame.image.load('resources/R2.png'), pygame.image.load('resources/R3.png'), pygame.image.load('resources/R4.png'), pygame.image.load('resources/R5.png'), pygame.image.load('resources/R6.png'), pygame.image.load('resources/R7.png'), pygame.image.load('resources/R8.png'), pygame.image.load('resources/R9.png')]
walkLeft = [pygame.image.load('resources/L1.png'), pygame.image.load('resources/L2.png'), pygame.image.load('resources/L3.png'), pygame.image.load('resources/L4.png'), pygame.image.load('resources/L5.png'), pygame.image.load('resources/L6.png'), pygame.image.load('resources/L7.png'), pygame.image.load('resources/L8.png'), pygame.image.load('resources/L9.png')]
bg = pygame.image.load('resources/bg.jpg')
char = pygame.image.load('resources/standing.png')

clock = pygame.time.Clock()

#Define Variables to represent our character
x = 50
y = 400
width = 40
height = 60
vel = 5

#add jumping
isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    # We have 9 images for our walking animation, I want to show the same image for 3 frames
    # so I use the number 27 as an upper bound for walkCount because 27 / 3 = 9. 9 images shown
    # 3 times each animation.
    global walkCount
    
    win.blit(bg, (0,0))  

    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  # If we are facing left
        win.blit(walkLeft[walkCount//3], (x,y))  # We integer divide walkCounr by 3 to ensure each
        walkCount += 1                           # image is shown 3 times every animation
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))  # If the character is standing still
        
    pygame.display.update() 
    


# Run until the user asks to quit
running = True

while running:
    clock.tick(27)  

    for event in pygame.event.get(): #This will loop thorugh a list of anykeyboard or mouse events

        if event.type == pygame.QUIT: #Check if the red button in the corner of the window is clicked
            running = False #End the game loop

    keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

    if keys[pygame.K_LEFT] and x > vel:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  # Making sure the top right corner of our character is less than the screen width - its width 
        x += vel
        left = False
        right = True

    else: # If the character is not moving we will set both left and right false and reset the animation counter (walkCount)
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False 
            left = False 
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False


    redrawGameWindow()
    
# Done! Time to quit.
pygame.quit()