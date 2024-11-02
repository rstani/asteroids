import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            center=self.position,
            radius=self.radius,
            width=2,
            color="white",
            surface=screen,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return "this was a small asteroid"
        else:
            r_angle = random.uniform(20, 50)
            new_vector_vel_1 = self.velocity.rotate(r_angle)
            new_vector_vel_2 = self.velocity.rotate(-r_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast_1.velocity = new_vector_vel_1 * 1.2
            new_ast_2.velocity = new_vector_vel_2 * 1.2
