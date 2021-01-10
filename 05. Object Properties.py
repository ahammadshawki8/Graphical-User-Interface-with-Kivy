# we have created a nice gui with kv language.
# But there is a problem with the button.
# how can we access the data and use trigger function?
# These we will see today.

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
# for using the object properties, we need to import ObjectProperty class
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name = ObjectProperty()
    email = ObjectProperty()
    message = ObjectProperty()
    # when we initially create this class there will be no object property.
    # so we have to use None which is default by the way.
    # Note this variables needs to be same as the varibles in the .kv file

    # Now we need to bind the button. first, lets create a method.
    def triggerprint(self): 
        # here we don't need to add instance arguement 
        # because root is automatically passed.
        name = self.name.text
        email = self.email.text
        message = self.email.text

        print("Name:", name, "\tEmail:", email, "\nMessage:", message)

        self.name.text = ""
        self.email.text = ""
        self.message.text = ""


class My5App(App):
    def build(self):
        return MyGrid()



if __name__ == "__main__":
    My5App().run()
