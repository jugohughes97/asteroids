import pygame
from constants import *
from player import Player
from meteor import Meteor
from meteormanager import MeteorManager

def main():


    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    print("Screen radius:", SCREEN_RADIUS)

    pygame.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    meteor_manager = MeteorManager()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable.add(player)
    drawable.add(player)

    run = True
    while True:

        clock = pygame.time.Clock()

        #gameloop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(meteor_manager.meteors)
                return
        screen.fill(0x000000)

        #update vars
        
        meteor_manager.update(player, dt)
        meteor_manager.draw(screen)
        for u in updatable:
            u.update(dt)
        for d in drawable:
            d.draw(screen)
        # player.update(dt)
        # player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

