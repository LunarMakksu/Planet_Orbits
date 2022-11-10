# Planet_Orbits
Python project for visualising planetary orbits in our solar system

# TEMPLATE
Using tutorial from youtuber [Tech With Tim](https://www.youtube.com/watch?v=WTLPmUHTPqo) 
and his [Repo](https://github.com/techwithtim/Python-Planet-Simulation) as a guide

What its supposed to look like:


<img src="https://github.com/LunarMakksu/Planet_Orbits/blob/main/resources/Screenshot%202022-11-09%20at%2013.55.55.png" width=320, length =300>


I plan to add the full 8 planets using the same class system.

For example:

```python
earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
earth.y_vel = 29.783 * 1000 
```

adding a displaysize multiplier to change the size of the planets in the visualizer, this will be relative to their real life sizes

Constructor:

```python
  def __init__(self, x, y, radius, colour, mass, displaysize):

            self.x = x
            self.y = y
            self.radius = radius
            self.colour = colour
            self.mass = mass
            self.displaysize = displaysize
```

Will fit into the size definition
```python
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
```
