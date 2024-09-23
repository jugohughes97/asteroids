import pygame
from constants import *
from asteroid import Asteroid
from random import randrange
class AsteroidManager:
    def __init__(self):
        self.asteroids = []
        self.timer = ASTEROID_SPAWN_RATE

    def generate_spawn(self):
        return pygame.Vector2(0, 1).rotate(randrange(0, 360, 1)).normalize() * SCREEN_RADIUS + (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    def add_asteroid(self, target):
        spawn = self.generate_spawn()
        self.asteroids.append(Asteroid(target, spawn.x, spawn.y))
    
    def remove_oldest(self):
        self.asteroids.remove(self.asteroids[0])

    def update(self, player, dt):
        self.timer -= dt
        if self.timer < 0:
            self.add_asteroid(player.position.copy())
            self.timer = ASTEROID_SPAWN_RATE
            
        for m in self.asteroids:
            m.update(dt)
            if m.collision(player):
                print("Game over!")
                print(self.asteroids)
                exit()

            for b in player.bullet_manager.fired_shots:
                if m.collision(b):
                    player.bullet_manager.remove_fired_shot(b)
                    x,y = m.split(player)
                    self.asteroids.remove(m)
                    if x is not None and y is not None:
                        self.asteroids.append(x)
                        self.asteroids.append(y)
                
            if m.is_beyond():
                self.asteroids.remove(m)
    
    def draw(self, screen):
        for m in self.asteroids:
            m.draw(screen)
