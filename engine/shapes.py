from engine.math2d import *
import numpy as np
import math

class Vec2(object):
    __doc__ = """
    Vec2(object) documentation:
        To initialize use "Vec2(optional: Iterable)" whereas Iterable is the length of two.
        It works with most operators too!  
    """
    
    def __init__(self, pos = (0,0)):
        if len(pos) == 2:self._vector = tuple(pos)
        else:raise IndexError("Length of positional argument must be exactly 2.")
    def __len__(self):return 2
    def __iter__(self):
        yield self.x
        yield self.y
    def __getitem__(self,i):
        if (i == 0):return self.x
        elif (i == 1):return self.y
        else:raise IndexError("Index needs to be 0 or 1!")
    def __setitem__(self,i,v):
        if (i == 0):self.x = v
        elif (i == 1):self.y = v
        else:raise IndexError("Index needs to be 0 or 1!")
        
    def __add__(self, x):
        if (type(x) == Vec2):return Vec2((self.x+x.x,self.y+x.y))
        else:return Vec2((self.x+x,self.y+x))
    def __sub__(self, x):
        if (type(x) == Vec2):return Vec2((self.x-x.x,self.y-x.y))
        else:return Vec2((self.x-x,self.y-x))
    def __truediv__(self, x):
        if (type(x) == Vec2):return Vec2((self.x/x.x,self.y/x.y))
        else:return Vec2((self.x/x,self.y/x))
    def __floordiv__(self,x):
        if (type(x) == Vec2):return Vec2((self.x//x.x,self.y//x.y))
        else:return Vec2((self.x//x,self.y//x))
    def __mul__(self, x):
        if (type(x) == Vec2):return Vec2((self.x*x.x,self.y*x.y))
        else:return Vec2((self.x*x,self.y*x))
    def __pow__(self, x):
        if (type(x) == Vec2):return Vec2((self.x^x.x,self.y^x.y))
        else:return Vec2((self.x^x,self.y^x))
    def __mod__(self, x):
        if (type(x) == Vec2):return Vec2((self.x%x.x,self.y%x.y))
        else:return Vec2((self.x%x,self.y%x))
    def __round__(self):return Vec2((round(self.x),round(self.y)))
    def __floor__(self):return Vec2((math.floor(self.x),math.floor(self.y)))
    def __ceil__(self):return Vec2((math.ceil(self.x),math.ceil(self.y)))
        
    __radd__ = __add__
    __rsub__ = __sub__
    __rtruediv__ = __truediv__
    __rfloordiv__ = __floordiv__
    __rmul__ = __mul__
    __rpow__ = __pow__
    __rmod__ = __mod__
        
    @property
    def x(self):return self._vector[0]
    @property
    def y(self):return self._vector[1]
    @property
    def xy(self):return self._vector
    @x.setter
    def x(self,x):self._vector=(float(x),self._vector[1])
    @y.setter
    def y(self,y):self._vector=(self._vector[0],float(y))
    @xy.setter
    def xy(self,pos):
        if len(pos) == 2:self._vector = tuple(pos)
        else:raise IndexError("Length of positional argument must be exactly 2.")

# Very basic Point class that acts like a point in 2d
class Point(object):
    def __init__(self,*args,screen=None,pos=Vec2((0,0)),scale=Vec2((1,1)),rotation=0,visible=False,**kwargs):
        self._pos = Vec2(pos)
        self.pos = self._pos
        self.scale = Vec2(scale)
        self.screen = screen
        self.rotation = rotation
        self.visible = bool(visible)
        
        # Check that we got a screen
        if (self.screen == None):raise AttributeError("Point.__init__() did not get required argument \"screen\"")
        else:self.screen.camera.objects.append(self)
    def render(self,frame,events):
        # Render the object
        return 0
    def isTouching(self,shape):
        # Do collision detection with other shapes
        return False
    def hovered(self):
        # Mouse hover detection
        return False
    @property
    def x(self):return self.pos[0]
    @property
    def y(self):return self.pos[1]
    @property
    def xy(self):return self.pos
    @x.setter
    def x(self,x):
        self._pos.x=x
        self.screen.camera.reloadXY(self)
    @y.setter
    def y(self,y):
        self._pos.y=y
        self.screen.camera.reloadXY(self)
    @xy.setter
    def xy(self,pos):
        if len(pos) == 2:
            self._pos = Vec2(pos)
            self.screen.camera.reloadXY(self)
        else:raise IndexError("Length of positional argument must be exactly 2.")

class Rectangle(Point):
    def __init__(self,*args,screen=None,color=(0,0,0),**kwargs):
        super().__init__(self,*args,screen=screen,**kwargs)
        self.color = color
    def render(self,frame,events):
        frame[self.x-(self.scale[0]/2):self.x+(self.scale[0]/2),self.y-(self.scale[1]/2):self.y+(self.scale[1]/2)] = self.color
        return 0
    def hovered(self):
        mx = self.screen.mouse.x
        my = self.screen.mouse.y
        return (((mx > self.x-(self.scale[0]/2)) and (mx < self.x+(self.scale[0]/2))) and ((my > self.y-(self.scale[1]/2)) and (my < self.y+(self.scale[1]/2))))
class Button(Rectangle):
    def __init__(self,*args,screen=None,color=(0,0,0),**kwargs):
        super().__init__(self,*args,screen=screen,**kwargs)
        self.color = color
        self.left = False
        self.right = False
        self.middle = False
        self.x1 = False
        self.x2 = False
    def render(self, frame, events):
        super().render(frame, events)
        self.left = (self.hovered() and self.screen.mouse.left)
        self.right = (self.hovered() and self.screen.mouse.right)
        self.middle = (self.hovered() and self.screen.mouse.middle)
        self.x1 = (self.hovered() and self.screen.mouse.x1)
        self.x2 = (self.hovered() and self.screen.mouse.x2)
        return 0