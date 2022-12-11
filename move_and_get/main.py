import pygame
import sys

SCREEN_WIDTH = 240
SCREEN_HEIGHT = 240

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("MOVE AND GET")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 120
pos_y = 120

clock = pygame.time.Clock()

class Enemy(object):
    def __init__(self):
        self.image = pygame.image.load("images/enemy_resize.png").convert_alpha()
        self.x = 30
        self.y = 30
        self.speed = 1
        self.direction = 1

    def move(self):
        global SCREEN_WIDTH
        self.x += self.speed * self.direction

        if self.x <= 0:
            self.x=0
            self.direction = 1
        
        if self.x+24 >= SCREEN_WIDTH:
            
            self.direction = -1
    
    def draw(self):
        global screen
        screen.blit(self.image, (self.x, self.y))

def main():
    enemy = Enemy()
    playerImage = pygame.image.load("images/player_resize.png").convert_alpha()
    global pos_x, pos_y, SCREEN_HEIGHT, SCREEN_WIDTH
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        key_event = pygame.key.get_pressed()
        if key_event[pygame.K_LEFT]:
            if pos_x > 0:
                pos_x -= 1

        if key_event[pygame.K_RIGHT]:
            if pos_x + 18 < SCREEN_WIDTH:
                pos_x += 1

        if key_event[pygame.K_UP]:
            if pos_y > 0:
                pos_y -= 1

        if key_event[pygame.K_DOWN]:
            if pos_y + 20 < SCREEN_HEIGHT:
                pos_y += 1
 

        screen.fill(black)

        enemy.move()
        enemy.draw()

        screen.blit(playerImage, (pos_x, pos_y))
        pygame.display.update()

if __name__ == "__main__":
    main()