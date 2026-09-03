from curses import COLOR_WHITE

import pygame
from pygame.color import Color

from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS

class  Player(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        radius = PLAYER_RADIUS
        super().__init__(x, y, radius)
        self.rotation = 0


    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "White", self.triangle(), LINE_WIDTH)
