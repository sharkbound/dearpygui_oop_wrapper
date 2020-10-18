from abc import abstractmethod
from typing import Any, Optional, Callable

from dpg_oop_wrapper.element import Element

__all__ = [
    'BaseButton'
]


class BaseButton(Element):
    def __init__(self, name: str, callback: Callable[[str, Any], None] = lambda _, __: None, callback_data: Optional[Any] = None, **config):
        super().__init__(name, **config)
        self.callback = callback
        self.callback_data = callback_data

    def on_clicked(self, sender: str, data: Any):
        if self.callback is not None:
            self.callback(sender, data)
