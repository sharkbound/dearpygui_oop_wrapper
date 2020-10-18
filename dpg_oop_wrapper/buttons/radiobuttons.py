from typing import Any, Optional, Callable

from dearpygui.core import add_same_line, add_radio_button

from .basebutton import BaseButton

__all__ = [
    'RadioButtons'
]


class RadioButtons(BaseButton):
    def __init__(self, name: str, *items: str, callback: Callable[[str, Any], None] = lambda _, __: None, callback_data: Optional[Any] = None,
                 default_index: int = 0, **config):
        super().__init__(name, callback=callback, callback_data=callback_data, **config)
        self.default_index = default_index
        self.items = list(items)

    @property
    def selected_value(self):
        return self.items[self.value]

    def place(self, same_line=False):
        if same_line:
            add_same_line()
        add_radio_button(self.name, items=self.items, default_value=self.default_index, callback=self.callback, callback_data=self.callback_data,
                         **self.default_config)
        return self
