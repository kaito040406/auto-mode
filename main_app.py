from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import subprocess as sb

 
class Widgets(Widget):
    def buttonClicked(self):
        # import trade
        pt = sb.Popen(["python", "trade.py"])
        # print("ok")
 
class main(App):
    def build(self):
        return Widgets()

if __name__ == "__main__":
    main().run()