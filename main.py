import pygame
import math
pygame.init()
#USING CODE TUTORIAL FROM https://github.com/techwithtim/Python-Planet-Simulation/blob/main/tutorial.py


WIDTH, HEIGHT = 1000, 770
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Sim")

#COLOUR RGB DECIMALS

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
LIGHT_BLUE = (173, 216, 230)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
ORANGE = (255,165,0)

FONT = pygame.font.SysFont("courier", 14)

class Planet:
    AU = 149.6e6 * 1000 #100 PIXELS

def main():
    run = True
    clock_elapsed = pygame.time.Clock()

    while run:
        clock_elapsed.tick(60)
        WIN.fill(BLUE)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


main()




