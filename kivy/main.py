#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from time import strftime
import time

import ss_local
import threading

class ShadowsocksApp(App):
    sw_started = False
    sw_seconds = 0

    
    def on_start(self):
        pass

    def update(self, nap):
        pass
        
    def start_stop(self):
        self.root.ids.start_stop.text = 'Start' if self.sw_started else 'Stop'
        self.sw_started = not self.sw_started
        threading.Thread(target=ss_local.main).start()

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False

        self.sw_seconds = 0

if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#45818e')
    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Thin.ttf',
                       fn_bold='Roboto-Medium.ttf')
    LabelBase.register(name='simsun',
                   fn_regular='simsun.ttc')
              
    ShadowsocksApp().run()
