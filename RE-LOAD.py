import pygame
import sys

# 1. Start Pygame
pygame.init()

# 2. Create the window (Width: 600, Height: 400)
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First Game Window")

# 3. Define a color using RGB (Red, Green, Blue)
# 0 Red, 128 Green, 255 Blue makes a nice light blue!
BACKGROUND_COLOR = (0, 128, 255) 

# 4. The Game Loop (Keeps the program running)
running = True
while running:
    
    # Listen for things the user does (like clicking the close button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # Stop the loop if they click 'X'

    # Color the whole screen
    screen.fill(BACKGROUND_COLOR)
    
    # Tell Pygame to update the window so we can see the changes
    pygame.display.flip()

# 5. Shut everything down when the loop ends
pygame.quit()
sys.exit()
rvt-rcrm-kpe
