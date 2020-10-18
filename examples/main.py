from dearpygui.simple import show_item

from dpg_oop_wrapper import *
from dearpygui.core import start_dearpygui

tools = Tab('tools')
other = Tab('other')
b1 = Button('hai!')
b2 = Button('bai!', callback=lambda *_: b2.hide())

with TabBar('tabbar'):
    with tools:
        tools.tooltip = 'testing!'
        b1.place()
    with other:
        b2.place()

start_dearpygui()
