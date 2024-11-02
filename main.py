import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for i in updatable:
            i.update(dt)
        for obj in asteroids:
            for bullet in shots:
                if bullet.col_checker(obj):
                    obj.split()
                    bullet.kill()
            if obj.col_checker(player1):
                print("Game Over")
                pygame.quit()
                sys.exit()
        screen.fill(BACKGROUND_COLOR)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()
