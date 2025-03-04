import pygame as p
from constants import *
from player import Player
import circleshape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    p.init()
    screen_set = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = p.time.Clock()
    dt = 0

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    
    updateables = p.sprite.Group()
    drawables = p.sprite.Group()
    asteroids = p.sprite.Group()
    shots = p.sprite.Group()

    
    Player.containers = (updateables, drawables)
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables)
    Shot.containers = (shots, updateables, drawables)

    player = Player(x,y)
    asteroid_field = AsteroidField()


    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                return

        p.Surface.fill(screen_set,(0,0,0))

        updateables.update(dt)

        for asteroid in asteroids:
            if asteroid.iscolliding(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.iscolliding(shot):
                    shot.kill()
                    asteroid.split()

        for obj in drawables:
            obj.draw(screen_set)
        
        p.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()