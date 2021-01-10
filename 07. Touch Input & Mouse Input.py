# In this module, we will learn about how to add mouse and touch input in our app.

from kivy.app import App
from kivy.uix.widget import Widget

# here we will create a class for touch input which is a subclass of Widget.
class Touch_past(Widget):
    # here we will create some functions.
    # These are parent functions, we will overweite them.
    def on_touch_down(self, touch):
        # when we press the button using mouse or touch,
        print("Mouse down", touch)
        # touch gives us spos and pos.
        # spos stands for relative position and pos stands for absolute position

    def on_touch_move(self, touch):
        # when we try to move press and hold on the object and move its position.
        print("Mouse move", touch)
        
    def on_touch_up(self, touch):
        # when we release toudh or mouse hold
        print("Mouse up", touch)
    
    # we can see that as we have overwrite this functions,
    # it doesn't have its default properties like color change.
    # we can set those properties by importing ObjectProperty

from kivy.properties import ObjectProperty

class Touch_past2(Widget):
    # Now we have create an instance of objectproperty
    btn = ObjectProperty()
    # and we also need to add a variable and id in the .kv file.

    def on_touch_down(self, touch):
        print("Mouse down", touch)
        # here we can change the properties
        self.btn.opacity = 0.5
        
    def on_touch_move(self, touch):
        print("Mouse move", touch)
        
    def on_touch_up(self, touch):
        print("Mouse up", touch)
        self.btn.opacity = 1

# we can also use the super() method to retrieve the properties from the parent class.
class Touch(Widget): 
    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        print("Mouse down", touch)
        
    def on_touch_move(self, touch):
        super().on_touch_move(touch)
        print("Mouse move", touch)
        
    def on_touch_up(self, touch):
        super().on_touch_up(touch)
        print("Mouse up", touch)


class My7App(App):
    def build(self):
        # returning Touch
        return Touch()

if __name__ == "__main__":
    My7App().run()