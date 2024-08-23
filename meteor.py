
import pygame
from random import randrange
from constants import *
from circleshape import CircleShape
class Meteor(CircleShape):
    def __init__(self, target, x, y): 
        super().__init__(x, y, self.randomize_meteor_radius())
        self.velocity = self.generate_vel(target.copy())

    def randomize_meteor_radius(self):
        return int(randrange(ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, 1))
    def draw(self, screen):
        pygame.draw.circle(screen, 0xFFFFFF, self.position, self.radius, width=2)
    def update(self, dt):
        self.position += self.velocity * dt
    def generate_vel(self, t):
        p = self.position
        v = pygame.Vector2(t.x-p.x,t.y-p.y)/4
        if v.length() < SCREEN_RADIUS / 2:
            v.scale_to_length(SCREEN_RADIUS / 2)
        return v