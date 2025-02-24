import pygame as p
from constants import *
import player
import circleshape

def main():
    p.init()
    screen_set = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = p.time.Clock()
    dt = 0

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    main_char = player.Player(x,y)

    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                return

        p.Surface.fill(screen_set,(0,0,0))

        main_char.update(dt)
        main_char.draw(screen_set)
        
        p.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()