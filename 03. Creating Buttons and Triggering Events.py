# here we will paste the code that we have in the previous module.
# and add other stuffs.

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button # for adding buttons


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.cols = 2
        
        self.add_widget(Label(text = "Name: "))
        self.name = TextInput(multiline = False) 
        # Note that here we can add multiple parameters.
        # we can change the font-group and size.
        # for more details, visit the official documentation.
        """https://kivy.org/doc/stable/#"""

        self.add_widget(self.name)

        self.add_widget(Label(text = "Email: "))
        self.email = TextInput(multiline = False) 
        self.add_widget(self.email)

        self.add_widget(Label(text = "Message: "))
        self.message = TextInput() 
        self.add_widget(self.message)

        # creating the button,
        self.submit = Button(text = "Submit")
        self.add_widget(self.submit)

        # we can see that we have created the button.
        # if we hover in the button, it will change its color.
        # we can click the button. However, nothing works now on click.
        # And the button position isn't what we wanted.
        # lets say we need to the submit button be placed in the middle.
        # that's kind of tough using GridLayout. 
        # Lets created another function and create that.


# The Interface will be something like this.
# -----------------------------------------
# |       Name       |                    |
# ----------------------------------------|
# |       Email      |                    |
# ----------------------------------------|
# |       Message    |                    |
# ----------------------------------------|
# |                                       |
# |                 Submit                |
# -----------------------------------------

# here first we have to create a GridLayout instance, 
# the NewMyGrid class will do this work.
# this instance will have 1 col and 2 rows.
# the last row will be our button.
# and inside of the first row, we will create another instance of GridLayout.
# that will have 2 col and 3 rows.
# here we will place our form data.
# NOTE: We have to use this technic a lot.


class NewMyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        # inside of the first row
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text = "Name: "))
        self.name = TextInput(multiline = False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text = "Email: "))
        self.email = TextInput(multiline = False) 
        self.inside.add_widget(self.email)

        self.inside.add_widget(Label(text = "Message: "))
        self.message = TextInput() 
        self.inside.add_widget(self.message)

        # outside of the first row
        self.add_widget(self.inside)

        self.submit = Button(text = "Submit", font_size = 40)
        self.add_widget(self.submit)

        # now lets add trigger function,
        # which will fire when we press the button.
        # for that we have to create a function in our class.
        # after we have created the function, we can connect the function to this button.
        # for connecting we need to use the bind function.
        self.submit.bind(on_press = self.triggerprint)
        # we need to fire the trigerprint() function on_press.

    def triggerprint(self, instance): 
        # note that we have to add an extra param instance.
        # instance is noting but the object name.
        # print(instance)

        # we can grab the value using text attribute
        name = self.name.text
        email = self.email.text
        message = self.email.text

        # now lets print the values only.
        print("Name:", name, "\tEmail:", email, "\nMessage:", message)

        # Now after completing this tasks, 
        # we dont want our form to hold the previous values.
        # so we can just set those values to empty string.
        self.name.text = ""
        self.email.text = ""
        self.message.text = ""



# Main class
class MyApp(App):
    def build(self):
        return NewMyGrid()


if __name__ == "__main__":
    MyApp().run()