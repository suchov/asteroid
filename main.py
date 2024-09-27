# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update method to update the ship dicretion on the button press
        player.update(dt)
        # define the screen color ...
        screen.fill(color='black', rect=None, special_flags=0)
        # re-render player on the screen
        player.draw(screen)
        # Update the display
        pygame.display.flip()
        # Limit the data to 60 FPS
        delta = clock.tick(60)
        # get the delta that we'll use later
        dt = delta / 1000


if __name__ == "__main__":

    main()
