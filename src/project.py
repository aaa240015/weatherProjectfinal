import pygame
import sys
import random
import math
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
class Bunny(Animal):
    '''''
    code break 🍹🍸
    This is from Wikipedia about rabbits/Bunnies::Disclaimer just to stop me from becoming one after this code😂😂
    Wikipedia::: Rabbits are small mammals in the family Leporidae, which is in the order Lagomorpha
    '''''
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed)
        self.ear_state =0
        self.ear_timer=0
        self.sit_timer=random.randint(60,180)
        self.is_sitting=True
        self.hop_state=0
        self.color_options=[
            {"body": (200, 200, 200), "belly": (240, 240, 240), "nose": (255, 150, 150)},
            {"body": (210, 180, 140), "belly": (230, 210, 180), "nose": (255, 150, 150)},
            {"body": (165, 145, 130), "belly": (200, 180, 160), "nose": (255, 150, 150)},
            {"body": (240, 240, 240), "belly": (255, 255, 255), "nose": (255, 150, 150)},
            {"body": (90, 90, 90), "belly": (130, 130, 130), "nose": (255, 150, 150)} 
        ]
        self.color = random.choice(self.color_options)
        self.size=random.uniform(0.8,1.2)
        self.speed = speed * 0.5
    def update(self):
        if not self.is_sitting:
            super().update()
            if self.hop_state <5:
                self.y=self.base_y- self.hop_state * 3 * math.sin(math.pi * self.hop_state/10)
            else:
                self.y = self.base_y - (10 - self.hop_state) * 3 * math.sin(math.pi * (10 - self.hop_state) / 10)
            self.hop_state = (self.hop_state + 1) % 10
            if random.random()<0.005:
                self.is_sitting=True
                self.sit_timer=random.randint(60,80)
        else:
            self.sit_timer-=1
            if self.sit_timer<=0:
                self.is_sitting=False
        self.ear_timer +=1
        if self.ear_timer>30:
            self.ear_timer=0
            self.ear_state=(self.ear_state+1) % 3
    def draw(self, screen):
        body_width=40* self.size
        body_height=20*self.size
        body_radius=12 * self.size
        body_rect=pygame.Rect(self.x - body_width/2, self.y - body_height/2, body_width, body_height)
        pygame.draw.ellipse(screen, self.colors["body"], body_rect)
        belly_width=body_width*0.7
        belly_height= body_height*0.7
        belly_rect =pygame.Rect(
            self.x - belly_width/2, 
            self.y - belly_height/2 + body_height * 0.1, 
            belly_width, 
            belly_height
        )
        pygame.draw.ellipse(screen,self.colors["belly"], belly_rect)
        head_x= self.x+15* self.direction*self.size
        pygame.draw.circle(screen, self.colors["body"], (int(head_x), int(self.y - 5 * self.size)), int(head_radius))
        eye_x = head_x + 4 * self.direction * self.size
        pygame.draw.circle(screen, BLACK, (int(eye_x), int(self.y - 8 * self.size)), int(3 * self.size))
        nose_x = head_x + 8 * self.direction * self.size
        pygame.draw.circle(screen, self.colors["nose"], (int(nose_x), int(self.y - 5 * self.size)), int(3 * self.size))
        for i in range(3):
            angle=(i-1)*0.2
            whisker_length = 10* self.size
            end_x = nose_x + math.cos(math.pi/2 + angle) * whisker_length * self.direction
            end_y = self.y - 5 * self.size + math.sin(math.pi/2 + angle) * whisker_length
            pygame.draw.line(screen, (100, 100, 100), (nose_x, self.y - 5 * self.size), (end_x, end_y), 1)
        ear_height = [25, 20, 15][self.ear_state] * self.size
        ear_width = 8 * self.size
        ear1_x = head_x - 5 * self.direction * self.size
        #im tired damn😂😂
        #implemnenig the ear of this bunny 🐇🐰
        pygame.draw.ellipse(screen, self.colors["body"], 
                           (ear1_x - ear_width/2, self.y - 30 * self.size, ear_width, ear_height))
        pygame.draw.ellipse(screen, (255, 200, 200), 
                           (ear1_x - ear_width/2 + 2, self.y - 30 * self.size + 2, ear_width - 4, ear_height - 4))
        ear2_x = head_x + 5 * self.direction * self.size
        #fun fact a bunny has two ears huh
        pygame.draw.ellipse(screen, self.colors["body"], 
                           (ear2_x - ear_width/2, self.y - 30 * self.size, ear_width, ear_height))
        pygame.draw.ellipse(screen, (255, 200, 200),
                                (ear2_x - ear_width/2 + 2, self.y - 30 * self.size + 2, ear_width - 4, ear_height - 4))
        if not self.is_sitting:
            leg_width=15 * self.size
            leg_height=10* self.size
            pygame.draw.ellipse(screen, self.colors["body"],
                                (self.x - body_width/2 - leg_width/2, self.y, leg_width, leg_height))
        tail_radius = 5 * self.size
        tail_x = self.x - body_width/2 * self.direction
        pygame.draw.Circle(screen, WHITE, (int(tail_x), int(self.y)), int(tail_radius))
##Well done to me 😁🍸🍸 go go Achai 

        

class Button:
    def __init__(self,x,y,width,height,text,color,hover_color,action=None,alpha=255):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color=hover_color
        self.action=action
        self.is_hovered=False
        self.aplha=alpha
    def handle_event(self,event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered=self.rect.collidepoint(event.pos)
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            if self.is_hovered and self.action:
                return self.action
        return None
    def draw(self,screen):
        button_surface=pygame.Surface((self.rect.width,self.rect.height),pygame.SRCALPHA)
        color = self.hover_color if self.is_hovered else self.color
        color_with_alpha = (color[0], color[1], color[2], self.alpha)
        pygame.draw.rect(button_surface, color_with_alpha, 
                        (0, 0, self.rect.width, self.rect.height), 
                        border_radius=10)
        pygame.draw.rect(button_surface, (0, 0, 0, self.alpha), 
                        (0, 0, self.rect.width, self.rect.height), 
                        2, border_radius=10)
        text_surface=main_font.render(self.text, True,BLACK)
        text_rect = text_surface.get_rect(center=(self.rect.width//2, self.rect.height//2))
        button_surface.blit(text_surface, text_rect)
        screen.blit(button_surface, self.rect)
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
