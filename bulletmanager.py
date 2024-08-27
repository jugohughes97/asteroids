from shot import Shot
from constants import *
class BulletManager:
    def __init__(self) -> None:
        self.magazine = [Shot(0,0) for _ in range(10)]
        self.fired_shots = []
    
    def reload(self):
        if len(self.magazine) < 10:
            self.magazine.append(Shot(0,0))
    
    def shoot(self, player):
        b = self.next_shot()
        if b is None:
            return
        b.shoot(player.get_position().x, player.get_position().y, player.rotation)
        self.fired_shots.append(b)

    def update(self, dt):
        for b in self.fired_shots:
            b.update(dt)
            x,y = b.position.x,b.position.y
            if x > SCREEN_WIDTH or x < 0 or y > SCREEN_HEIGHT or y < 0:
                self.fired_shots.remove(b)
                
    
    def draw(self, screen):
        for b in self.fired_shots:
            b.draw(screen)

    def next_shot(self):
        if len(self.magazine) > 0:
            return self.magazine.pop()
        return None

    def remove_fired_shot(self, b):
        if b in self.fired_shots:
            self.fired_shots.remove(b)