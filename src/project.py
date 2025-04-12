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
