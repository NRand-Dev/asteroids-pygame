# from tkinter import constants

import pygame
import sys
#from pygame.color import Color
import asteroidfield
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Initalize the game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    # Create pygame groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Player is the name of the class, not an instance of it
    # This must be done before any Player objects are created
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    # Create inital objects
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2, 2)
    asteroid_field = AsteroidField()
    dt = 0.0

    # While pygame is running, call log state.
    while pygame.get_init() == True:
        log_state()
        # Process pygame event queue.
        for event in pygame.event.get():
            # Quit Button Handling
            if event.type == pygame.QUIT:
                return

        # Draw the screen
        screen.fill("black")
        # Calculate delta time capping at 60 FPS.
        dt = clock.tick(60) / 1000



        # Update the groups
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        for item in asteroids:
            if item.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                # Close the game
                sys.exit()
            else:
                continue

        # Refresh the screen
        pygame.display.flip()




## Keep this here. This line ensures that the main function is only called when this file is run directly.
# Would not be ran if imported.
# Considered proper structure for python.
if __name__ == "__main__":
    main()
