import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
import matplotlib.ticker as ticker


class Grid(object):
    def __init__(self, initial, w, h):
        self.state = initial

        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)
        self.w = w
        self.h = h

        self.arm = plt.Rectangle((0, 0), 1, 1, fc='r')
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
        self.arm.xy = ((x+1) % self.w, (y+1) % self.h) 
        return (self.line,)

    def play(self):
        anim = animation.FuncAnimation(self.fig, self.plot_step, init_func=self.init, frames=50, interval=200)        
        plt.grid(True)
        plt.show()



initial = [(0,0), (0,1), (0,2)]
grid = Grid(initial, 10, 10)

grid.play()