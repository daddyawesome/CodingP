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

    if keys[pygame.K_LEFT] and x > vel:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - vel - width:  # Making sure the top right corner of our character is less than the screen width - its width 
        x += vel

    if keys[pygame.K_UP] and y > vel:  # Same principles apply for the y coordinate
        y -= vel

    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel
        
    win.fill((0,0,0))  # Fills the screen with black to make the block looks like it is moving
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update()
    
# Done! Time to quit.
pygame.quit()