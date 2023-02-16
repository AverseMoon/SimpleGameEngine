from math2d import *
import numpy as np

class Vec2(object):
    def __init__(self,pos):
        if len(pos) == 2:self._vector = tuple(pos)
        else:raise IndexError("Length of positional argument must be exactly 2.")
    def __len__(self):return 2
    def __iter__(self):
        yield self.x
        yield self.y
    @property
    def x(self):return self._vector[0]
    @property
    def y(self):return self._vector[1]
    @property
    def xy(self):return self._vector
    @x.setter
    def x(self,x):self._vector=(x,self._vector[1])
    @y.setter
    def y(self,y):self._vector=(self._vector[0],y)
    @xy.setter
    def xy(self,pos):
        if len(pos) == 2:self._vector = tuple(pos)
        else:raise IndexError("Length of positional argument must be exactly 2.")

# Very basic Point class that acts like a point in 2d
class Point(object):
    def __init__(self,screen=None,pos=(0,0),scale=(1,1),rotation=0):
        self.pos = Vec2(pos)
        self.scale = Vec2(scale)
        self.screen = screen
        self.rotation = rotation
        
        # Check that we got a screen
        if (self.screen == None):raise AttributeError("Point.__init__() did not get required argument \"screen\"")
        else:self.screen.camera.objects.append(self)
    def render(self,frame):
        # Render the object
        frame
    def isTouching(self,shape):
        # Do collision detection with other shapes
        return False
    def hover(self):
        # Mouse hover detection
        return False