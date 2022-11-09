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


#displaysize:
#scale of 1->5, 1 being the smallest planet size e.g. mars and 5 being the largest, jupiter, this will affect planet size on the visualizer.

def DisplaySize(size):
    if size == 1:
        return 0.8
    elif size == 2:
        return 1.4
    elif size == 3:
        return 1.6
    elif size == 4:
        return 2.1
    elif size == 5:
        return 2.5
#--------------------------------------------------------------------------------------------------------------------------------------------

class Planet:
        AU = 149.6e6 * 1000 #100 PIXELS is one ASTRONOMICAL UNIT
        G = 6.67428e-11
        SCALE = 250 / AU  # 1AU = 100 pixels
        TIMESTEP = 3600*24 # 1 day

        def __init__(self, x, y, radius, colour, mass, displaysize):

            self.x = x
            self.y = y
            self.radius = radius
            self.colour = colour
            self.mass = mass
            self.displaysize = displaysize

            self.orbit = []
            self.sun = False
            self.distance_to_sun = 0

            self.x_vel = 0
            self.y_vel = 0

        def drawPlanet(self, win):
                x = self.x * self.SCALE + WIDTH / 2
                y = self.y * self.SCALE + HEIGHT / 2

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




