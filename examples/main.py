from dearpygui.simple import show_item

from dpg_oop_wrapper import *
from dearpygui.core import start_dearpygui

with TabBar('tabbar'):
    with Tab('tools') as tools:
        tools.tooltip = 'testing!'
        b1 = Button('hai!').place()
    with Tab('other'):
        b2 = Button('bai!', callback=lambda *_: b2.hide()).place()

start_dearpygui()
