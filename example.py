from engine import screen, shapes
import numpy as np

newScreen = screen.Screen(title = "Cheap MS Paint!!!",size=(480,480))

class FadingRect(shapes.Rectangle):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,color=np.array((255,255,255)),**kwargs)
        self.tick = 0
    def render(self,frame,events):
        super().render(frame,events)
        self.color[:] -= 1
        if (self.tick == 255):return 1
        self.tick += 1
        return 0

@newScreen.onDraw
def draw(events,frame):
    frame[:,:] = (0,0,0) # Fill the screen with black
    if (newScreen.mouse.left): # If mouse down
        FadingRect(screen=newScreen,scale=(20,20),pos=newScreen.mouse.xy) # Make new rectangle that fades out
    return 0 # Return 1 to quit

newScreen.run()