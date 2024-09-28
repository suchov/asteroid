import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # span new asteroids in different directions
        random_angle = random.uniform(20, 50)
        # create new vectors for asteroids
        first_new_vector = self.velocity.rotate(random_angle)
        second_new_vector = self.velocity.rotate(-random_angle)
        # new asteroid size
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # create new asteroids
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = first_new_vector * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = second_new_vector * 1.2
