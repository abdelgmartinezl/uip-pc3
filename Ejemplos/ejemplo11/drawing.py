from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class DrawingSpace(RelativeLayout):
   pass
   
class DrawingApp(App):
   def build(self):
      return DrawingSpace()

if __name__=="__main__":
   DrawingApp().run()
