# SimpleGameEngine

For the people who don't like UI's.

# Tutorials

### Setup:

Start with a simple import and initialization.
```python
import SimpleGameEngine
import sdl2
import sdl2.ext as sdl
from SimpleGameEngine.engine import screen

def frame(events,frame):
    pass # put your before draw code here

game = screen.Screen(title="Tutorial game", update=frame) # you can use the icon attribute to change the icon, 
game.run()
```