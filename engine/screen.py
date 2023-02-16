import sdl2.ext as sdl
import sdl2, cv2, numpy as np
import image as img
import shapes
from cython import cfunc, cclass, returns, locals as flocals
import cython as cy
import opensimplex as sim

sdl.init()

@cclass
class Camera:
    def __init__(self, screen):
        self._pos = shapes.Vec2((0,0)) # Position of center of screen
        self.objects = []
    @cfunc
    def render(self,frame):
        for object in self.objects:object.render(frame,self)


@cclass
# Screen, the window to the world!
class Screen:
    def __init__(self,width=220,height=229,title="Simple Game",icon="././images/icon.png",flags=sdl2.SDL_WINDOW_RESIZABLE):
        self.camera = Camera(self)
        self.window = sdl.Window(title, size=(width,height), flags=flags)
        self.update = []
        self.running = False
        self.setIcon(icon)
    
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
            frame = img.Frame(np.zeros((s[1],s[0],3),dtype=np.uint8))
            for func in self.update:
                if (func(events,frame)):
                    self.running = False
                    break
            for event in events:
                if (event.type == sdl2.SDL_QUIT):
                    self.running = False
                    break
            self.camera.render(frame)
            try:np.copyto(arr,np.flip(np.rot90(np.insert(frame.array,3,255,axis=2)),axis=0))
            except:pass
            self.window.refresh()
        self.window.hide()


if __name__ == '__main__':
    s = Screen(title="test")
    
    @s.onDraw
    def update(evts,frame):
        frame[:,:50] = (255,0,255)
    @s.onDraw
    def update2(evts,frame):
        frame[:,:25] = (0,0,255)
    
    s.run()