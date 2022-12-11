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

def main():
    global pos_x, pos_y, SCREEN_HEIGHT, SCREEN_WIDTH
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        key_event = pygame.key.get_pressed()
        if key_event[pygame.K_LEFT]:
            pos_x -= 1

        if key_event[pygame.K_RIGHT]:
            pos_x += 1

        if key_event[pygame.K_UP]:
            pos_y -= 1

        if key_event[pygame.K_DOWN]:
            pos_y += 1

        screen.fill(black)
        pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
        pygame.display.update()

if __name__ == "__main__":
    main()