import pygame
from circleshape import CircleShape
from constants import *
from bulletmanager import BulletManager
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x,y)
        self.rotation = 0
        self.bullet_manager = BulletManager()
        self.rof = PLAYER_ROF
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 0xFFFFFF, self.triangle(), 2)
        self.bullet_manager.draw(screen)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.rof -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE] and self.rof <= 0:
            self.bullet_manager.shoot(self)
            self.rof = PLAYER_ROF
        if keys[pygame.K_r]:
            self.bullet_manager.reload()

        self.bullet_manager.update(dt)
    
    def move(self, dt):
        self.position += pygame.Vector2(0,1).rotate(self.rotation) * dt * PLAYER_MOVE_SPEED
    
    def get_position(self):
        return self.position