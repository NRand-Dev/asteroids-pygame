# from tkinter import constants

from tkinter import CENTER

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
import shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Initalize the game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    score = 0 # Initalize score
    font = pygame.font.SysFont("arial", 36, True) # Choose font and size. True makes it bold.


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
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                # Close the game
                sys.exit()
            else:
                # Check for shot collison
                for shot in shots:
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")
                        asteroid.split() # Break asteroid
                        score += 1 # Update score

                        shot.kill() # Destory shot


        # Render and display score
        text = font.render("Score: " + str(score), 1, (255,255,255))
        text_center = text.get_rect(center=(SCREEN_WIDTH / 2, 40))
        # Screen width is trying to set the x position of the text.
        # Currently, Screen_width is a constant of 1280. And starting the score at the halfway point makes it look off center.
        # I will need to find a way to get the current size of the pygame screen. Divide it by 2. And subtract an offset equal to half of the texts length.
        screen.blit(text, text_center)


        # Refresh the screen
        pygame.display.flip()




## Keep this here. This line ensures that the main function is only called when this file is run directly.
# Would not be ran if imported.
# Considered proper structure for python.
if __name__ == "__main__":
    main()
