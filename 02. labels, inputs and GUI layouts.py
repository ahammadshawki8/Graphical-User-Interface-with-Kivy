# first lets import couple of things.
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
# this will help us to work on the layout.
# there are different types of layouts in kivy.
# but we will use GridLayout here.
from kivy.uix.textinput import TextInput

# in previous module, we just returned a Label.
# but it is not practical. What if we need to return multile labels.
# for that purpose, we need to create another class.
# this class will hold all of our design elements.
class MyGrid(GridLayout):
    # GridLayout have grids where we can add items.
    # it have certain amount of rows and columns.
    # here we have to create an __init__() mehtod.
    def __init__(self, **kwargs):
        # we can pass many keyword arguements.
        # now we have to manage the parameters using the default constructor.
        # for that we need to use the super() method.
        super(MyGrid, self).__init__(**kwargs)
        # super() takes 2 arguements.
        # here the type arguement is this class name. and the obj arguement will be self.
        # we can also ignore the arguements, python will set the arguements for us.
        
        self.cols = 2
        # setting coloumn number in the grid
        # we can change this value and see what happens

        # now lets add few widgets we can do this my add_widget() function.
        self.add_widget(Label(text = "Name: "))
        # the the add_widget function we can add different types of widgets.
        # we can also pass the Label.
        # now we have set up a label named Name.
        # now we need to ask for input, in kivy we can do that using TextInput() 
        self.name = TextInput(multiline = False) 
        # here we set the multiline arguement to false 
        # because we don't need to have multiline inputs for name.
        # now we need to add this self.name varible (which is a TextInput widget) to our Grid.
        self.add_widget(self.name)
        # Now lets add few more widgets 
        self.add_widget(Label(text = "Email: "))
        self.email = TextInput(multiline = False) 
        self.add_widget(self.email)
        self.add_widget(Label(text = "Message: "))
        self.message = TextInput() 
        self.add_widget(self.message)



# creating the main class
class MyApp(App):
    def build(self):
        # here we will return MyGrid() class
        return MyGrid()


# Now lets run the app.
if __name__ == "__main__":
    MyApp().run()
    # we can see that we have a part for our input()
    # we can resize the window.
    # also we can input strings.
    # But we cant use multiline in name and email.