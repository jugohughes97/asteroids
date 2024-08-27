import pygame
from constants import *
from meteor import Meteor
from random import randrange
class MeteorManager:
    def __init__(self):
        self.meteors = []
        self.timer = ASTEROID_SPAWN_RATE

    def generate_spawn(self):
        return pygame.Vector2(0, 1).rotate(randrange(0, 360, 1)).normalize() * SCREEN_RADIUS + (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    def add_meteor(self, target):
        spawn = self.generate_spawn()
        self.meteors.append(Meteor(target, spawn.x, spawn.y))
    
    def remove_oldest(self):
        self.meteors.remove(self.meteors[0])

    def update(self, player, dt):
        self.timer -= dt
        if self.timer < 0:
            self.add_meteor(player.position.copy())
            self.timer = ASTEROID_SPAWN_RATE
            
        for m in self.meteors:
            m.update(dt)
            if m.collision(player):
                print("Game over!")
                print(self.meteors)
                exit()

            for b in player.bullet_manager.fired_shots:
                if m.collision(b):
                    player.bullet_manager.remove_fired_shot(b)
                    self.meteors.remove(m)
            
            if m.is_beyond():
                self.meteors.remove(m)
    
    def draw(self, screen):
        for m in self.meteors:
            m.draw(screen)
