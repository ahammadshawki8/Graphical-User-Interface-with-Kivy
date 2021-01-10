# kivy has its own design language, which name is KV language.
# It is simmilar to css, the file extension is .kv
# it provides us functionalities to create applications in a lot easier way.
# so, we will use KV language to recreate the exact thing that we created before.
# so first we need to create a styling file in .kv extension
# as our main class name is myApp, our styling file name will be my.kv
# for naming .kv files, the name will be the lowercase version of the main class,
# and if we the main class name ends with App, we need to ignore the App.
# for naming and numbering purpose, I am changing the name of my main class.

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# we have to import the Widget class
from kivy.uix.widget import Widget


# this MyGrid class is a sub class of Widget
class MyGrid(Widget):
    pass


class My4App(App):
    def build(self):
        return MyGrid()



if __name__ == "__main__":
    My4App().run()

