import kivy
from kivy.app import App
# since we will work with multiple screens so we need to import screen, screen manager.
from kivy.uix.screenmanager import Screen, ScreenManager

# Now here we will have few classes that will represent each screen.
class MainWindow(Screen):
    # these will represent our main window a login form.
    def check_pass(self, email):
        if email == "ahammadshawki8@gmail.com":
            return "1234"
    pass

class SecondWindow(Screen):
    # these will represent our second window where we will move after the login.
    pass

class WindowManager(ScreenManager):
    # windw manager will manage all the windows,
    # here we will define the transitions and that kind of stuff.
    pass

# Notice that, our class name is MyMainApp but our kv file name is my9
# so, it won't load the kv file automatically.
# for loading kivy file we need to import a builder
from kivy.lang import Builder

# here we have to load the file.
kv = Builder.load_file("my9.kv")
class MyMainApp(App):
    def build(self):
        # here we will return the kv file
        return kv

if __name__ == "__main__":
    MyMainApp().run()