# in this module, we will create an popup window,
# they are very useful.
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
# first we need to import popup
from kivy.uix.popup import Popup

# because we have a popup, we need to show something in the popup.
# so we need to create a class.
class Pop(FloatLayout):
    # it will inherit from FloatLayout.
    # we will add widgets in this class using the .kv file.
    pass

# now we will create a function which will create a popup window for us.
def show_popup():
    # the content of this popup is the Pop class.
    show = Pop() # creating an instance of Pop class

    # creating a popupWindow
    popupWindow = Popup(title = "Popup Window", content = show, size_hint = (0.6, 0.3))
    # here we have to pass the title, the content and the size.
    # we have to also set the size hint, otherwise it will cover the entire window.
    # we can also pass the pos, but by default the pos is middle of the screen which is nice.

    # Now to show this window we dont have to add this in the Widgets class.
    # all we have to do is to use open() function.
    popupWindow.open()

# Now we have this popup window, but how can we trigger this window.
# we can create a widget inside our Widgets class, ideally a button.
# And when we press that button we will trigger that show_popup function. 

class Widgets(Widget):
    # first creating the trigger method
    def btn(self):
        show_popup()

    # Now we will create the button in the .kv file.



class My10App(App):
    def build(self):
        return Widgets()



if __name__ == "__main__":
    My10App().run()