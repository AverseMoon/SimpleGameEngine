import sdl2.ext as sdl
import sdl2, numpy as np
from .image import Frame
from cython import cfunc, cclass, returns, locals as flocals
import cython as cy
from .shapes import Vec2
from .simplemouse import Mouse

sdl.init()



@cclass
class Camera:
    def __init__(self, screen):
        self._pos = Vec2((0,0)) # Position of center of screen
        self.objects = []
        self.screen = screen
    @cfunc
    def render(self,frame,events):
        for i,obj in enumerate(self.objects):
            if (not obj.visible):
                self.reloadXY(obj)
                if (obj.render(frame,events) == 1):del self.objects[i]
    def reloadXY(self,obj):
        obj.pos = obj._pos
        obj.pos.x -= self._pos.x
        obj.pos.x -= self._pos.y


@cclass
# Screen, the window to the world!
class Screen:
    def __init__(self,size=Vec2((220,229)),title="Simple Game",icon="././images/icon.png",flags=sdl2.SDL_WINDOW_RESIZABLE):
        self.camera = Camera(self)
        self.window = sdl.Window(title, size=tuple(size), flags=flags)
        self.update = []
        self.running = False
        self.setIcon(icon)
        self.mouse = Mouse()
    
    @property
    def width(self):return self.window.size[0]
    @property
    def height(self):return self.window.size[1]
    @property
    def wh(self):return self.window.size
    @width.setter
    def width(self,v):self.window.size = (v,self.window.size[1])
    @height.setter
    def height(self,v):self.window.size = (self.window.size[0],v)
    @wh.setter
    def wh(self,v):self.window.size = tuple(v)
    
    def refreshIcon(self):sdl2.SDL_SetWindowIcon(self.window.window, sdl.image.load_img(self.icon))
    def setIcon(self, icon):
        self.icon = icon
        self.refreshIcon()
    def onDraw(self,function):
        self.update.append(function)
        def decor(*args,**kwargs):return function(*args,**kwargs)
        return decor
    @cfunc
    def run(self):
        renderer = sdl.Renderer(self.window)
        self.window.show()
        self.running = True
        
        while self.running:
            windowSurf = sdl2.SDL_GetWindowSurface(self.window.window)
            arr = sdl2.ext.pixels3d(windowSurf.contents)
            events = sdl.get_events()
            s = self.window.size
            frame = Frame(np.zeros((s[1],s[0],3),dtype=np.uint8))
            for func in self.update:
                if (func(events,frame) == 1):
                    self.running = False
                    break
            for event in events:
                if (event.type == sdl2.SDL_QUIT):
                    self.running = False
                    break
            self.camera.render(frame,events)
            try:np.copyto(arr,np.flip(np.rot90(np.insert(frame.array,3,255,axis=2)),axis=0))
            except:pass
            self.window.refresh()
        self.window.hide()