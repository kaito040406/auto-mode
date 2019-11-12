from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import subprocess as sb
import os

 
class Widgets(Widget):
    def buttonClicked1(self):
        global tl
        tl = sb.Popen(["python", "trade.py"])
        bottan_st = 1

    def buttonClicked2(self):
        tl.terminate()
        # os.kill(pt.pid, signal.SIGINT)
        bottan_st = 0
 
class main(App):
    def build(self):
        return Widgets()

if __name__ == "__main__":
    main().run()