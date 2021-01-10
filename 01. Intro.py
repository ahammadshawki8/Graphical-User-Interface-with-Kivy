# kivy is a python library which allows us to create pretty standard and minimal GUI
# which can be use in all types of devices.

# for using kivy first we need to install it using pip.
"""
pip install kivy.deps.gstreamer
pip install kivy.deps.angle
pip install kivy
pip install pygame
"""
# pygame is necessary as we will use it in the kivy window.

# so first lets import kivy
import kivy
# if we run the file, we can see few info messages. That's totally fine.

# now lets see what kivy has for us.
print(dir(kivy))
# we can see that we have lots of different functions here.

# we also need to import App
from kivy.app import App
# here App is a class. we can tell that by the CamelCasing
# this will help us to create apps

# we also have to use widgets and labels in our app.
# we need to import another class.
from kivy.uix.label import Label
# here uix is a folder and label is a module and Label is a class


# kivy actually works in the object oriented approach.
# so first we have to create a class that will inherit from the App class.

class MyApp(App):
    # here we will create a build class. 
    # The reason we do not need an init() method because it is predifend in the parent App class.
    def build(self):
        # now we will return Lable() function and it takes text arguement.
        return Label(text = "My First App")

# And the last thing we need to do is to run our app.
if __name__ == "__main__":
    MyApp().run()
    # here we need to includes the brackets MyApp() because
    # MyApp() doesn't have any run() method in it.
    # instead MyApp() is a arguement used in the run() method.
    # this run method() will setup everything, configure all graphics
    