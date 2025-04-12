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

##now for the rainy weather ill have some frogs jumping here and there
class Frog(Animal):
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed)
        self.jump_state = 0
        self.jump_height = 0
        self.jump_timer = random.randint(30, 120)
        self.color_options = [
            {"body": (34, 139, 34), "spots": (25, 100, 25), "belly": (200, 220, 200)},
            {"body": (107, 142, 35), "spots": (85, 107, 47), "belly": (220, 230, 200)},
            {"body": (60, 179, 113), "spots": (46, 139, 87), "belly": (200, 255, 200)},
            {"body": (85, 107, 47), "spots": (60, 80, 30), "belly": (180, 200, 160)},
            {"body": (143, 188, 143), "spots": (133, 173, 133), "belly": (220, 240, 220)}
        ]
        self.colors = random.choice(self.color_options)
        self.size = random.uniform(0.8, 1.2)
        self.blink_timer = 0
        self.is_blinking = False
    def update(self):
        if self.jump_state>0:
            self.x+=self.speed *2 * self.direction
            if self.jump_state<10:
                self.jump_height=self.jump_state *4 *math.sin(math.pi * self.jump_state / 20)
            else:
                self.jump_height = (20 - self.jump_state) * 4 * math.sin(math.pi * (20 - self.jump_state) / 20)
            self.y = self.base_y - self.jump_height
            self.jump_state += 1
            if self.jump_state >= 20:
                self.jump_state = 0
                self.jump_timer = random.randint(30, 120)
        else:
            self.jump_timer -= 1
            if self.jump_timer <= 0:
                self.jump_state = 1
        if self.x < 50 or self.x > WIDTH - 50:
            self.direction *= -1
        self.blink_timer+=1
        if self.blink_timer>120:
            self.is_blinking=True
            if self.blink_timer>125:
                self.is_blinking=False
                self.blink_timer=0
    def draw(self, screen):
        body_radius=15*self.size
        pygame.draw.circle(screen, self.colors["body"], (self.x, self.y), int(body_radius))
        for _ in range(5):
            spot_x = self.x + random.uniform(-body_radius/2, body_radius/2)
            spot_y = self.y + random.uniform(-body_radius/2, body_radius/2)
            spot_radius = random.uniform(2, 4) * self.size
            if (spot_x - self.x)**2 + (spot_y - self.y)**2 < (body_radius*0.8)**2:
                pygame.draw.circle(screen, self.colors["spots"], (int(spot_x), int(spot_y)), int(spot_radius))
        eye_offset = 8 * self.direction * self.size
        eye_y_offset = -10 * self.size
        eye_radius = 5 * self.size
        pygame.draw.circle(screen, WHITE, 
                          (int(self.x + eye_offset), int(self.y + eye_y_offset)), 
                          int(eye_radius))
        pygame.draw.circle(screen, WHITE, 
                          (int(self.x + eye_offset - 5 * self.direction * self.size), int(self.y + eye_y_offset)), 
                          int(eye_radius))
        if not self.is_blinking:
            pupil_radius=2*self.size
            pygame.draw.circle(screen, BLACK, 
                              (int(self.x + eye_offset), int(self.y + eye_y_offset)), 
                              int(pupil_radius))
            pygame.draw.circle(screen, BLACK, 
                              (int(self.x + eye_offset - 5 * self.direction * self.size), int(self.y + eye_y_offset)), 
                              int(pupil_radius))
        else:
            pygame.draw.line(screen, BLACK, 
                            (int(self.x + eye_offset - eye_radius), int(self.y + eye_y_offset)),
                            (int(self.x + eye_offset + eye_radius), int(self.y + eye_y_offset)),
                            2)
            pygame.draw.line(screen, BLACK, 
                            (int(self.x + eye_offset - 5 * self.direction * self.size - eye_radius), int(self.y + eye_y_offset)),
                            (int(self.x + eye_offset - 5 * self.direction * self.size + eye_radius), int(self.y + eye_y_offset)),
                            2)
            mouth_width=10*self.size
            pygame.draw.arc(screen, (50,50,50),
                          (self.x - mouth_width/2, self.y, mouth_width, 5 * self.size),
                       0,math.pi,2)
            if self.jump_state ==0:
                leg_width = 20 * self.size
                leg_height = 10 * self.size
                pygame.draw.ellipse(screen, self.colors["body"], 
                               (self.x - leg_width - 5 * self.size, self.y + 5 * self.size, leg_width, leg_height))
                pygame.draw.ellipse(screen, self.colors["body"], 
                               (self.x + 5 * self.size, self.y + 5 * self.size, leg_width, leg_height))
                arm_width=12 * self.size
                arm_height=6* self.size
                pygame.draw.ellipse(screen, self.colors["body"], 
                               (self.x - arm_width/2 - 10 * self.size, self.y - 2 * self.size, arm_width, arm_height))
                pygame.draw.ellipse(screen, self.colors["body"], 
                               (self.x - arm_width/2 + 10 * self.size, self.y - 2 * self.size, arm_width, arm_height))
        #This reminds me of the story of the frog and the princess... i wonder if they wrote a code like this to do the animation
            else:
                leg_height=20*self.size
                leg_width =5 *self.size
                pygame.draw.line(screen, self.colors["body"], 
                            (self.x - 10 * self.size, self.y), 
                            (self.x - 25 * self.size, self.y + 20 * self.size), 
                            int(leg_width))
                pygame.draw.line(screen, self.colors["body"], 
                            (self.x + 10 * self.size, self.y), 
                            (self.x + 25 * self.size, self.y + 20 * self.size), 
                            int(leg_width))
                foot_width=10* self.size
                foot_height= 5 * self.size
                pygame.draw.ellipse(
                    screen,
                    self.colors["body"],
                    (self.x - 25 * self.size - foot_width/2, self.y + 20 * self.size - foot_height/2, 
                                foot_width, foot_height)
                )
                pygame.draw.ellipse(screen,
                                     self.colors["body"], 
                               (self.x + 25 * self.size - foot_width/2,
                                 self.y + 20 * self.size - foot_height/2, 
                                foot_width, 
                                foot_height))
                pygame.draw.line(screen, 
                                 self.colors["body"], 
                            (self.x - 5 * self.size, 
                             self.y - 5 * self.size), 
                            (self.x - 15 * self.size,
                              self.y - 10 * self.size), 
                            int(leg_width * 0.7))
                pygame.draw.line(screen, 
                                 self.colors["body"], 
                            (self.x + 5 * self.size, 
                             self.y - 5 * self.size), 
                            (self.x + 15 * self.size,
                              self.y - 10 * self.size), 
                            int(leg_width * 0.7))



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
