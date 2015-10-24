from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

import time

class Reloj(Label):
    def update(self, *args):
        self.text = time.asctime()

class TiempoApp(App):
    def build(self):
        reloj = Reloj()
        Clock.schedule_interval(reloj.update, 1)
        return reloj

if __name__ == "__main__":
    TiempoApp().run()
