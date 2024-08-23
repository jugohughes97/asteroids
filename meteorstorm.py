import pygame
from constants import *
from meteor import Meteor
from random import randrange
class MeteorStorm:
    def __init__(self):
        self.meteors = []


    def generate_spawn(self):
        return pygame.Vector2(0, 1).rotate(randrange(0, 360, 1)).normalize() * SCREEN_RADIUS + (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    def add_meteor(self, target):
        spawn = self.generate_spawn()
        self.meteors.append(Meteor(target, spawn.x, spawn.y))
    
    def remove_oldest(self):
        self.meteors.remove(self.meteors[0])

    def update(self, player_pos, dt):
        if pygame.time.get_ticks() % 1800 > 0 and pygame.time.get_ticks() % 1800 < 50:
            self.add_meteor(player_pos)
            if len(self.meteors) > 20:
                self.remove_oldest()
            
        for m in self.meteors:
            m.update(dt)
    
    def draw(self, screen):
        for m in self.meteors:
            m.draw(screen)
