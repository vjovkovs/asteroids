# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   # Initialize pygame
    pygame.init()
    
    # Create a window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game loop
    while True:
        # Check for player inputs (event handling)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update the game world
        # (This will be implemented in future steps)
        
        # Draw the game to the screen
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()