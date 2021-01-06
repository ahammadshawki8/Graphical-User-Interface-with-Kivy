# here we will paste the code that we have in the previous module.
# and add other stuffs.

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.cols = 2
        
        self.add_widget(Label(text = "Name: "))
        self.name = TextInput(multiline = False) 
        self.add_widget(self.name)

        self.add_widget(Label(text = "Email: "))
        self.email = TextInput(multiline = False) 
        self.add_widget(self.email)

        self.add_widget(Label(text = "Message: "))
        self.message = TextInput() 
        self.add_widget(self.message)



# Main class
class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()