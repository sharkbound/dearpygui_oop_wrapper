from ..element import Element
from dearpygui.core import add_tab, end

__all__ = [
    'Tab'
]


class Tab(Element):
    def __init__(self, name: str, closable: bool = False, **config):
        super().__init__(name, **config)
        self.closable = closable

    def place(self, same_line=False):
        raise RuntimeError("don't use place() with Tab, use the class with a WITH block instead: ex: with Tab('test'): ...")

    def _add(self):
        add_tab(self.name, closable=self.closable, **self.default_config)

    def start(self):
        self._add()

    def end(self):
        end()

    def __enter__(self):
        self._add()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end()
