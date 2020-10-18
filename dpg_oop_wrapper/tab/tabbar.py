from ..element import Element
from dearpygui.core import add_tab_bar, end, add_same_line

__all__ = [
    'TabBar'
]


class TabBar(Element):
    def __init__(self, name: str, reorderable: bool = False, **config):
        super().__init__(name, **config)
        self.reorderable = reorderable

    def place(self, same_line=False):
        raise RuntimeError("don't use place() with TabBar, use the class with a WITH block instead: ex: with TabBar('test'): ...")

    def _add(self):
        add_tab_bar(self.name, reorderable=self.reorderable, **self.default_config)

    def start(self):
        self._add()

    def end(self):
        end()

    def __enter__(self):
        self._add()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end()
