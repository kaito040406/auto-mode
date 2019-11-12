from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import subprocess as sb

global bottan_st = 0
 
class Widgets(Widget):
    def buttonClicked1(self):
        if bottan_st == 0:
            global tl
            tl = sb.Popen(["python", "trade.py"])
            global bottan_st = 1
        else:
            pass

    def buttonClicked2(self):
        if bottan_st == 1:
            tl.terminate()
            global bottan_st = 0
        else:
            pass
 
class main(App):
    def build(self):
        return Widgets()

if __name__ == "__main__":
    main().run()