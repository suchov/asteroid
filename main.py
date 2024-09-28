# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # shots group
    Shot.containers = (shots, updatable, drawable)


    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update method to update the ship dicretion on the button press
        for obj in updatable:
            obj.update(dt)
        # stop the game if colide
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        # check if asteroids meet with the bullets
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

        # define the screen color ...
        screen.fill(color='black', rect=None, special_flags=0)
        # re-render player on the screen
        for obj in drawable:
            obj.draw(screen)
        # Update the display
        pygame.display.flip()
        # Limit the data to 60 FPS
        delta = clock.tick(60)
        # get the delta that we'll use later
        dt = delta / 1000

if __name__ == "__main__":

    main()
