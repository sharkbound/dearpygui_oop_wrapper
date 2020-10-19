from typing import Any

from dpg_oop_wrapper import *
from dearpygui.core import start_dearpygui, add_text


class ButtonSubClass(Button):
    def on_clicked(self, sender: str, data: Any):
        print('this is the callback from overriding on_clicked in Button class')


def cb_button_class_button(sender, data):
    print('this is the callback from callback= in Button class init')


with TabBar('tabbar'):
    with Tab('main tab'):
        add_text('buttons:')
        button_subclass = ButtonSubClass('subclass button').place()
        button_class_button = Button('button class button', callback=cb_button_class_button).place()
        radio_buttons = RadioButtons('radio buttons',
                                     'value 1', 'value 2', 'value 3',
                                     callback=lambda *_: print(f'{radio_buttons.selected_value} has been selected!')).place()

        add_text('\n\ninputs:')
        text_input = TextInput('text input').place()
        int_input = IntInput('int input', count=4).place()
        float_input = FloatInput('float input', count=4).place()

start_dearpygui()
