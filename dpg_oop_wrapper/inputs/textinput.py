from typing import Callable, Optional, Any

from dearpygui.core import add_input_text, add_same_line
from ..element import Element

__all__ = [
    'TextInput'
]


class TextInput(Element):
    def __init__(self, name: str,
                 default_value: str = '',
                 multiline: bool = False,
                 hex: bool = False,
                 password: bool = False,
                 readonly: bool = False,
                 decimal: bool = False,
                 no_spaces: bool = False,
                 uppercase: bool = False,
                 scientific: bool = False,
                 callback_on_enter: bool = True,
                 callback: Callable[[str, Any], None] = lambda _, __: None,
                 callback_data: Optional[Any] = None, **config):
        super().__init__(name, multiline=multiline, default_value=default_value, password=password,
                         readonly=readonly, on_enter=callback_on_enter, hexadecimal=hex, decimal=decimal,
                         no_spaces=no_spaces, uppercase=uppercase, scientific=scientific, **config)
        self.default_value = default_value
        self.callback = callback
        self.callback_data = callback_data

    def on_text_changed(self, sender: str, data: Any):
        if self.callback is not None:
            self.callback(sender, data)

    def place(self, same_line=False):
        if same_line:
            add_same_line()
        add_input_text(self.name, callback=self.on_text_changed, callback_data=self.callback_data, **self.default_config)
        return self

    def reset_text_to_default(self):
        self.value = self.default_value
