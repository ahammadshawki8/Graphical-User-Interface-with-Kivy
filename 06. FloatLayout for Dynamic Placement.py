# in this module, we will learn about the float layout.
# the grif layout was nice, but there are some issues with resizeabilities.
# float layout is better than grid layout, it will run on all os especially phones.

from kivy.app import App
# importing FloatLayout
from kivy.uix.floatlayout import FloatLayout

class My6App(App):
    def build(self):
        # instead of creating a subclass and returning that,
        # we will return the FloatLayout.
        return FloatLayout()

if __name__ == "__main__":
    My6App().run()

# thats actually all we need to do within our python script,
# now we will go to our .kv file.