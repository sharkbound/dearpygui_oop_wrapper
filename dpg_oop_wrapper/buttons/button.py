from typing import Callable, Any, Optional

from .basebutton import BaseButton
from dearpygui.core import add_button, add_same_line

__all__ = [
    'Button'
]


class Button(BaseButton):
    def place(self, same_line=False):
        if same_line:
            add_same_line()
        add_button(self.name, callback=self.on_clicked, callback_data=self.callback_data, **self.default_config)
        return self
