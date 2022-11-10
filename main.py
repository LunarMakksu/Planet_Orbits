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
DARK_BLUE = (5, 0, 159)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
ORANGE = (255,165,0)
BLACK = (0, 0 , 0)

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
        TIMESTEP = 3600*12 # 1/2 day

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


                if len(self.orbit) > 2:
                    updated_points = []
                    for point in self.orbit:
                        x, y = point
                        x = x * self.SCALE + WIDTH / 2
                        y = y * self.SCALE + HEIGHT / 2
                        updated_points.append((x, y))

                    pygame.draw.lines(win, self.colour, False, updated_points, 2)
                    pygame.draw.circle(win, self.colour, (x, y), self.radius)

                    if not self.sun:
                        distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, DARK_BLUE)
                        win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

 

        def attraction_angle(self, other):
            other_x, other_y = other.x, other.y
            distance_x = other_x - self.x
            distance_y = other_y - self.y
            distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
            theta = math.atan2(distance_y, distance_x)
            return theta


        def attraction_force(self, other):
            other_x, other_y = other.x, other.y
            distance_x = other_x - self.x
            distance_y = other_y - self.y
            distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

            if other.sun:
                self.distance_to_sun = 0 #was distance

            force = self.G * self.mass * other.mass / distance**2
            
            theta = math.atan2(distance_y, distance_x)
            force_x = math.cos(theta) * force
            force_y = math.sin(theta) * force
            return force_x, force_y
                        
        def Arrow(self, other):
            self.x = other.x
            self.y = other.y
            self.colour = other.colour



    
        def update_position(self, planets):
            total_fx = total_fy = 0
            for planet in planets:
                if self == planet:
                    continue
                fx, fy = self.attraction_force(planet)
                theta = self.attraction_angle(planet)
                total_fx += fx
                total_fy += fy

            self.x_vel += total_fx / self.mass * self.TIMESTEP
            self.y_vel += total_fy / self.mass * self.TIMESTEP

            self.x += self.x_vel * self.TIMESTEP
            self.y += self.y_vel * self.TIMESTEP
            self.orbit.append((self.x, self.y))






def main():
    run = True
    clock_elapsed = pygame.time.Clock()

    while run:
        clock_elapsed.tick(60)
        WIN.fill(DARK_BLUE)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


main()




