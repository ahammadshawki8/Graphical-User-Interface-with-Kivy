# In this module, we will create a simple drawing application.
# there will be square object that will more in the screen if we hover the mouse.
# and when we click the mouse, it will print the object.

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
# first we need to import graphics for drawing
from kivy.graphics import Rectangle
from kivy.graphics import Color
# so graphics in kivy is based on openGL
# there we have canvas and that canvas contains drawing instuctions
# we can update the instructions to move the object.

# we can also create a line
from kivy.graphics import Line


class Touch(Widget):
    # here we have to define the __init__ method.
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # now here we need to draw a rectangle and we can do that with context manager.
        with self.canvas: # Widget have a canvas property
            # changing the color of the canvas.
            Color(1, 0, 0, 0.5, mode="rgba")

            # creating Rectangle instance
            self.rect = Rectangle(pos = (0,0), size = (50,50))
            # here we have pass pos and size both are tuple.
            # if we need to chnage the color of the object.
            # we have to change the color for the entire canvas.
            
            # NOTE that, we have placed the rectangle in a static position.
            # if we change the width nad height of the kivy window from the right and down,
            # the position change.
            # otherwise it remains at the same position.  

            # Creating a line.
            Line(points = ((0,100),(100,0),(400,500))) 
            # it takes bunch of (x,y) points and connect them. 


    def on_touch_down(self, touch):
        # Now here we will chnage the property of the rectangle object.
        self.rect.pos = touch.pos
        super().on_touch_down(touch)

    def on_touch_move(self, touch):
        # Same thing
        self.rect.pos = touch.pos
        super().on_touch_move(touch)



class My8App(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    My8App().run()