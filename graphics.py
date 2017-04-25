import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
import matplotlib.ticker as ticker

class Arm:
    def __init__(self, w, h, arm_w):
        points = [[0, 0], [0, h], [w, h], [w, 0], [w-1, 0], [w-1, h-1], ]
        line = plt.Polygon(points, closed=None, fill=None, edgecolor='r')

class Grid(object):
    def __init__(self, initial, w, h):
        self.state = initial

        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)
        self.w = w
        self.h = h

        self.arm = plt.Rectangle((0, 0), 1, 1, fc='r')
        self.arm.set_clip_on(False)
        plt.gca().add_patch(self.arm)

    
    # initialization function: plot the background of each frame
    def init(self):
        self.ax.set_xlim(( 0, self.w))
        self.ax.set_ylim(( 0, self.h))
        loc = ticker.MultipleLocator(1)
        self.ax.xaxis.set_major_locator(loc)
        self.ax.yaxis.set_major_locator(loc)
        return (self.line,)
    
    def step(self):
        # TODO: Game of Life implementation goes here
        # Either assign a new value to self.state, or modify it
        return None


    def plot_step(self, i):
        self.step()
        x, y = self.arm.xy
        self.arm.xy = ((x+0.05) % (self.w+2), (y+0.05) % (self.h+2)) 
        return (self.line,)

    def play(self):
        anim = animation.FuncAnimation(self.fig, self.plot_step, init_func=self.init, frames=1000, interval=100)        
        plt.grid(True)
        plt.show()



initial = [(0,0), (0,1), (0,2)]
grid = Grid(initial, 10, 10)

grid.play()