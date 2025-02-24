import pygame as p
from constants import *

def main():
    p.init()
    screen_set = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                return
            
        p.Surface.fill(screen_set,(0,0,0))
        p.display.flip()

if __name__ == "__main__":
    main()