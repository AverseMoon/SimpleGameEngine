from math2d import *
import numpy as np

# Very basic Point class that acts like a point in 2d
class Point:
    def __init__(self,screen=None,pos=(0,0),scale=(1,1),rotation=0):
        self.pos = pos
        self.scale = scale
        self.screen = screen
        self.rotation = rotation
        
        # Check that we got a screen
        if (self.screen == None):raise AttributeError("Point.__init__() did not get required argument \"screen\"")
        else:self.screen.addShape(self)
    def render(self):
        # Render the object
        pass
    def collide(self,shape):
        # Do collision detection with other shapes
        return False
    def hover(self):
        # Mouse hover detection
        return False