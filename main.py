# from tkinter import constants

import pygame
#from pygame.color import Color
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Initalize the game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2, 2)



    # While pygame is running, call log state.
    while pygame.get_init() == True:
        log_state()
        # Process pygame event queue.
        for event in pygame.event.get():
            # Quit Button Handling
            if event.type == pygame.QUIT:
                return

        clock = pygame.time.Clock()
        # Draw the screen
        screen.fill("black")
        dt = clock.tick(60) / 1000

        # Draw the player
        player.draw(screen)
        # Refresh the screen
        pygame.display.flip()




## Keep this here. This line ensures that the main function is only called when this file is run directly.
# Would not be ran if imported.
# Considered proper structure for python.
if __name__ == "__main__":
    main()
