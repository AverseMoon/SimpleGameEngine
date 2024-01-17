## NOTE THAT:
This version is not updated anymore and will probably be switched to a wrapper for the new version [SimpleGameEngineC++](https://github.com/AverseMoon/SimpleGameEngineCPP)


# SimpleGameEngine
For the people who don't like UIs


### Cheap Microsoft Paint:

Start with a simple import and initialization.
```python
from SimpleGameEngine.engine import screen,shapes
import numpy as np
```
Next make a screen.
```python
MyScreen = screen.Screen(title="My Simple Game") # make a screen with the title: "My Simple Game"
```
Make a button, and a key event in the frame function
```python
button = shapes.Button(screen = MyScreen, pos = MyScreen.center, scale = (50,30), color = (255,255,255))
# White button that is 50x30 pixels in the center of the screen

@MyScreen.onDraw # onDraw function decorator running your function every frame
def onUpdateEvent(events,frame): # This function will be ran ONCE per frame
    button.xy = MyScreen.center # Force button to stay at center of screen even after rescaling!
    if MyScreen.keyDown("space"): # If the SPACE button is pressed?
        newRect = shapes.Rectangle(screen = MyScreen, pos = MyScreen.mouse.xy, color = np.random.randint(0, 255, size = (3)), scale = (20,20)) 
        # Make a 20 x 20 pixel rectangle at the mouse's position when space is pressed
    if button.left: # If the button is left clicked
        pos = (np.random.randint(0, MyScreen.width), np.random.randint(0, MyScreen.height))
        newRect = shapes.Rectangle(screen = MyScreen, pos = pos, color = np.random.randint(0, 255, size = (3)),scale = (20,20))

    frame[:,:] = (255,255,0) # Fill the screen with cyan aka (0,255,255) in rgb, sdl uses bgr, just the reverse.
```
Last step, run the game:
```python
MyScreen.run()
```
Now just run the python program and you have a 5⭐ Microsoft Paint competitor!
