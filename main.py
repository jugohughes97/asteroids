import pygame
from constants import *
from player import Player



def main():


    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)

    pygame.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    while True:
        clock = pygame.time.Clock()
        
        #gameloop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0x000000)

        #update vars
        player.update(dt)

        #refresh display
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

