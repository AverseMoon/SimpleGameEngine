import sdl2.ext as sdl
import sdl2, cv2, numpy as np

sdl.init()


# Screen, the window to the world!
class Screen:
    def __init__(self,width=220,height=229,title="Simple Game",update=lambda evts:0,flags=sdl2.SDL_WINDOW_RESIZABLE):
        self.loadedImages = {}
        self.window = sdl.Window(title, size=(width,height), flags=flags)
        self.update = update
        self.running = False
    def run(self):
        windowSurf = sdl2.SDL_GetWindowSurface(self.window.window)
        arr = sdl2.ext.pixels3d(windowSurf.contents)
        self.window.show()
        self.running = True
        
        while self.running:
            events = sdl.get_events()
            s = self.window.size
            frame = np.zeros((s[1],s[0],3),dtype=np.uint8)
            if (self.update(events)):
                self.running = False
                break
            for event in events:
                if (event.type == sdl2.SDL_QUIT):
                    self.running = False
                    break
            try:np.copyto(arr,np.flip(np.rot90(np.insert(frame,3,255,axis=2)),axis=0))
            except:pass
            self.window.refresh()
        self.window.hide()
        return
                

s = Screen()
s.run()