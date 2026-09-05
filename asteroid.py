import random

import pygame
from pygame.math import Vector2

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen: pygame.Surface) -> None:
        # Draw the circle
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt: float) -> None:
        # Getting the velocity from the CicleShape class
        self.position += (self.velocity * dt)

    def split(self) -> None:
        # Kill the asteroid that was hit.
        self.kill()
        # Check for small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Otherwise it is a Medium or Large asteroid.
        # If medium or large, destroy self, but spawn 2 new asteroids.
        elif self.radius > ASTEROID_MIN_RADIUS:
            # Log the event
            log_event("asteroid_split")
            # Generate a random angle between 20 and 50 degrees.
            angle = random.uniform(20,50)
            # Set velocity angle and radius.
            asteroid_1_vector = Vector2.rotate(self.velocity, angle)
            asteroid_2_vector = Vector2.rotate(self.velocity, -angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

            # Create new asteroids
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)

            # The 1.2 multiplication speeds up the vector/velocity.
            asteroid_1.velocity = (asteroid_1_vector * 1.2)
            asteroid_2.velocity = (asteroid_2_vector * 1.2)
