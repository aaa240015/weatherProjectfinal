import pygame
import sys
import random
pygame.init()
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Weather Environment Simulator")

BLUE = (135, 206, 235)
DARK_BLUE = (25, 25, 112)
GRAY = (119, 136, 153)
DARK_GRAY = (47, 79, 79)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GREEN = (34, 139, 34)
BROWN = (139, 69, 19)
FPS = 60
clock = pygame.time.Clock()
try:
    title_font = pygame.font.Font(None, 48)
    main_font = pygame.font.Font(None, 32)
    small_font = pygame.font.Font(None, 24)
except:
    title_font = pygame.font.SysFont(None, 48)
    main_font = pygame.font.SysFont(None, 32)
    small_font = pygame.font.SysFont(None, 24)
def draw_cloud(screen, x, y, width, height, color):
    ellipse_rect = pygame.Rect(x, y, width, height)
    pygame.draw.ellipse(screen, color, ellipse_rect)
    pygame.draw.ellipse(screen, color, pygame.Rect(x + width*0.2, y - height*0.3, width*0.6, height*0.6))
    pygame.draw.ellipse(screen, color, pygame.Rect(x + width*0.4, y - height*0.2, width*0.4, height*0.6))
class Animal:
    def __init__(self,x,y,speed):
        self.x=x
        self.y=y
        self.speed=speed
        self.direction=1 if random.random() >0.5 else -1
        self.base_y=y
    def update(self):
        self.x += self.speed*self.direction
        if self.x<0 or self.x>WIDTH:
            self.direction *=-1
    def draw(self,screen):
        pass
class Bird(Animal):
    def __init__(self,x,y,speed):
        super().__init__(x,y,speed)
        self.wing_state=0
        self.wing_timer=0
        self.color_options=[
            {"body":(50,50,50),"wing":(30,30,30),"beak":(255,165,0)},
            {"body": (165, 42, 42), "wing": (120, 30, 30), "beak": (255, 200, 0)},
            {"body": (70, 130, 180), "wing": (30, 80, 140), "beak": (255, 255, 0)},
            {"body": (107, 142, 35), "wing": (85, 107, 47), "beak": (255, 140, 0)},
            {"body": (220, 20, 60), "wing": (180, 20, 40), "beak": (255, 215, 0)},
            {"body": (255, 215, 0), "wing": (218, 165, 32), "beak": (255, 140, 0)}
        ]
        self.color=random.choice(self.color_options)
        self.size=random.uniform(0.8,1.2)
        self.flight_offset=random.uniform(-20,20)
        self.wing_speed=random.uniform(0.8,1.2)
    def update(self):
        super().update()
        self.y = self.base_y + math.sin(self.x / 50) * 15 + self.flight_offset
        self.wing_timer += 1 * self.wing_speed
        if self.wing_timer>5:
            self.wing_timer=0
            self.wing_state=(self.wing_state + 1)%4
    def draw(self, screen):
        body_width =30*self.size
        body_height=15* self.size
        head_radius=8 * self.size
        eye_radius =2 * self.size
        pygame.draw.ellipse(screen,self.colors["body"],
                            (self.x-body_width/2, self.y-body_height/2,
                             body_width,body_height)
                            )
        head_x=self.x+(head_radius+5)*self.direction
        pygame.draw.circle(screen, self.colors["body"], 
                          (int(head_x), int(self.y)), 
                          int(head_radius))
        eye_x = head_x + 2 * self.direction
        pygame.draw.circle(screen, WHITE, 
                          (int(eye_x), int(self.y - 2)), 
                          int(eye_radius))
        pygame.draw.circle(screen, BLACK, 
                          (int(eye_x), int(self.y - 2)), 
                          int(eye_radius/2))
        beak_length = 6*self.size
        beak_height=4*self.size
        beak_points=[
            (head_x + head_radius * self.direction, self.y),
            (head_x + (head_radius + beak_length) * self.direction, self.y - beak_height/2),
            (head_x + (head_radius + beak_length) * self.direction, self.y + beak_height/2)
        ]
        pygame.draw.polygon(screen, self.colors["beak"],beak_points)
        tail_width=12* self.size
        tail_height=10*self.size
        tail_x=self.x-body_width/2 - tail_width/2 *self.direction
        tail_points =[
            (self.x - body_width/2 * self.direction, self.y),
            (tail_x - tail_width/2 * self.direction, self.y - tail_height/2),
            (tail_x - tail_width * self.direction, self.y),
            (tail_x - tail_width/2 * self.direction, self.y + tail_height/2)
        ]
        pygame.draw.polygon(screen, self.colors["body"], tail_points)
        wing_width = 20 * self.size
        wing_height = 10 * self.size
        if self.wing_state == 0:
            wing_y = self.y - body_height/2 - wing_height
            wing_angle = -20
        elif self.wing_state == 1:
            wing_y = self.y - body_height/4 - wing_height/2
            wing_angle = -10
        elif self.wing_state == 2:
            wing_y = self.y + body_height/4
            wing_angle = 10
        else:
            wing_y = self.y + body_height/2
            wing_angle = 20
        wing_surface = pygame.Surface((wing_width, wing_height), pygame.SRCALPHA)
        pygame.draw.ellipse(wing_surface, self.colors["wing"], 
                           (0, 0, wing_width, wing_height))
        rotated_wing = pygame.transform.rotate(wing_surface, wing_angle * self.direction)
        wing_rect = rotated_wing.get_rect(center=(self.x, wing_y))
        screen.blit(rotated_wing, wing_rect)


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
