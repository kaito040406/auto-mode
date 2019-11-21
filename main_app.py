from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import subprocess as sb
from kivy.config import Config
from kivy.uix.textinput import TextInput

Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '960')  
Config.set('graphics', 'resizable', False)  
 

 
class Widgets(Widget):
    def buttonClicked1(self):
        global tl
        tl = sb.Popen(["python", "trade.py"])

    def buttonClicked2(self):
        tl.terminate()
 
class main(App):
    def build(self):
        return Widgets()

if __name__ == "__main__":
    main().run()