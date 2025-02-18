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
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)    
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots,updatables, drawables)
    
    asteroidfield = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    #groups


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatables.update(dt)
        
        
        screen.fill("black")

        for asteroid in asteroids:
            #player collides with asteroid(s)
            if player.collided(asteroid):
                print("Game over!")
                sys.exit()

            #asteroid collides with bullet
            for bullet in shots:
                if bullet.collided(asteroid):
                    asteroid.split()
                    bullet.kill()
        #for drawable in drawables:
        for drawable in drawables:
            drawable.draw(screen)
        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
       

if __name__ == "__main__":
    main()
