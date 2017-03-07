#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, \
    with_statement
from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from time import strftime
import time
from shadowsocks import local
import ss_local
import threading
from multiprocessing import Process

class start_ss_local():
    def run():
        Process(target=ss_local.main).start()

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
        start_ss_local.run()

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False

        self.sw_seconds = 0

if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#45818e')
    LabelBase.register(name='Roboto',
                       fn_regular='res/Roboto-Thin.ttf',
                       fn_bold='res/Roboto-Medium.ttf')
    LabelBase.register(name='simsun',
                       fn_regular='res/simsun.ttc')

    ShadowsocksApp().run()
