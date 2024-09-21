from constants import *
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self,x,y,radius=SHOT_RADIUS):
        super().__init__(x,y,radius)
        self.velocity = PLAYER_MOVE_SPEED * 2
        self.rotation = None
        self.is_active = False
    
    def shoot(self, x,y,rotation):
        self.position = pygame.Vector2(x,y)
        self.rotation = rotation
        self.is_active = True

    def update(self, dt):
        if self.is_active:
            #update position
            self.position += pygame.Vector2(0,1).rotate(self.rotation) * dt * self.velocity
            

    def draw(self, screen):
        if self.is_active:
            pygame.draw.circle(screen, 0xFFFFFF, self.position, self.radius, 1)