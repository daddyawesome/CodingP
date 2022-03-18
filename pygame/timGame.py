# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
win = pygame.display.set_mode([500, 500])
pygame.display.set_caption("First Game")

#Define Variables to represent our character
x = 50
y = 50
width = 40
height = 60
vel = 5

# Run until the user asks to quit
running = True

while running:
    pygame.time.delay(100)  #this will delay the game the given amount of millisecond. 0.1 sec will be the delay

    for event in pygame.event.get(): #This will loop thorugh a list of anykeyboard or mouse events

        if event.type == pygame.QUIT: #Check if the red button in the corner of the window is clicked
            running = False #End the game loop

    keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

    if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update()
    
# Done! Time to quit.
pygame.quit()