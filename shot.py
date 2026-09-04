
import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        radius = SHOT_RADIUS
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        # Draw the circle
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt: float) -> None:
        # Getting the velocity from the CicleShape class
        self.position += (self.velocity * dt)
