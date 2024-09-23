
import pygame
import sys
from random import randrange
from constants import *
from circleshape import CircleShape
class Asteroid(CircleShape):
    
    def __init__(self, target = None, x = SCREEN_WIDTH, y = SCREEN_HEIGHT, radius_func = randomize_meteor_radius, vel = pygame.Vector2(0,0)): 
        
        super().__init__(x, y, radius_func())
        if target is None:
            self.velocity = vel
        else:
            self.velocity = self.generate_vel(target.copy())
        self.lu = self.find_lu()
    
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
    
    def find_lu(self):
        x, y =self.position.x, self.position.y
        xh, yh = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
        return x < xh and y < yh
        
    def is_beyond(self):
        x, y =self.position.x, self.position.y
        sw, sh = SCREEN_WIDTH, SCREEN_HEIGHT
        r = self.radius
        if self.lu == (True,True):
            return x + r > sw and y + r > sh
        elif self.lu == (False,True):
            return x+r < 0 and y + r > sh
        elif (True,False):
            return x+r > sw and y+r < 0
        else:
            return x+r < 0 and y+r < 0
        # else:

        #     x, y =self.position.x, self.position.y
        #     sw, sh = SCREEN_WIDTH, SCREEN_HEIGHT
        #     r = self.radius
        #     match self.lu:
        #         case True,True:
        #             return x + r > sw and y + r > sh
        #         case False,True:
        #             return x+r < 0 and y + r > sh
        #         case True,False:
        #             return x+r > sw and y+r < 0
        #         case other:
        #             return x+r < 0 and y+r < 0

    def split(self, t):
        if self.radius - ASTEROID_MIN_RADIUS < ASTEROID_MIN_RADIUS:
            return None, None
        a,b = Asteroid(x = self.position.x,y = self.position.y, radius_func = lambda: self.radius - ASTEROID_MIN_RADIUS, vel=self.velocity),Asteroid(x = self.position.x,y = self.position.y, radius_func = lambda: self.radius - ASTEROID_MIN_RADIUS, vel=self.velocity)
        angle_to = int(self.velocity.angle_to(self.velocity))
        a.velocity = a.velocity.rotate(randrange(angle_to-40, angle_to+40, 5))
        b.velocity = b.velocity.rotate(randrange(angle_to-40, angle_to+40, 5))
        return a,b