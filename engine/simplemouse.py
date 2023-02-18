import sdl2.ext.mouse as sdl
from .shapes import Vec2

class Mouse:
    @property
    def bstate(self):return sdl.mouse_button_state()
    @property
    def visible(self):return sdl.cursor_hidden()
    @property
    def x(self):return sdl.mouse_coords()[0]
    @property
    def y(self):return sdl.mouse_coords()[1]
    @property
    def xy(self):return Vec2(sdl.mouse_coords())
    @property
    def delta(self):return Vec2(sdl.mouse_delta())
    @property
    def left(self):return self.bstate.left
    @property
    def right(self):return self.bstate.right
    @property
    def middle(self):return self.bstate.middle
    @property
    def x1(self):return self.bstate.x1
    @property
    def x2(self):return self.bstate.x2
    @x.setter
    def x(self,x):sdl.warp_mouse(x,self.y)
    @y.setter
    def y(self,x):sdl.warp_mouse(x,self.y)
    @xy.setter
    def xy(self,xy):sdl.warp_mouse(xy.x,xy.y)
    
    def hide(self):sdl.hide_cursor()
    def show(self):sdl.show_cursor()