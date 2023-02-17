from engine import screen, shapes

newScreen = screen.Screen(title = "Hello World!")

point = shapes.Point(newScreen) # Create a point (appears as rectangle because of testing purposes)

@newScreen.onDraw
def draw(events,frame):
    frame[:,:] = (0,255,0) # Fill the screen with BGR color pallette GREEN
    point.xy = newScreen.mouse.xy
    return 0 # Return 1 to quit

newScreen.run()