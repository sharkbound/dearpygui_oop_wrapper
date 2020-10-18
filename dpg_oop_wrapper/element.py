from abc import ABCMeta, abstractmethod
from typing import TypeVar

from dearpygui.core import (
    is_item_hovered,
    is_item_active,
    is_item_shown,
    is_item_focused,
    is_item_visible,
    is_item_toggled_open,
    is_item_activated,
    is_item_deactivated,
    is_item_edited,
    is_item_clicked,
    is_item_container,
    is_item_deactivated_after_edit,
    get_value,
    configure_item,
    set_value,
    get_item_children,
    get_item_configuration
)

__all__ = [
    'Element'
]

PlaceType = TypeVar('PlaceType')


class Element(metaclass=ABCMeta):
    def __init__(self, name: str, **config):
        self.name = name
        self.default_config = config

    @property
    def tooltip(self) -> str:
        return get_item_configuration(self.name).get('tip', '')

    @tooltip.setter
    def tooltip(self, tooltip: str):
        self.configure(tip=tooltip)

    def show(self):
        configure_item(self.name, show=True)

    def hide(self):
        configure_item(self.name, show=False)

    def configure(self, **config):
        configure_item(self.name, **config)
        return self

    @abstractmethod
    def place(self, same_line=False):
        """
        places the element in the GUI then returns itself
        :param same_line:
        """
        return self

    @property
    def children(self):
        return get_item_children(self.name)

    @property
    def value(self):
        return get_value(self.name)

    @value.setter
    def value(self, new_value):
        set_value(self.name, new_value)

    @property
    def is_hovered(self):
        return is_item_hovered(self.name)

    @property
    def is_active(self):
        return is_item_active(self.name)

    @property
    def is_shown(self):
        return is_item_shown(self.name)

    @property
    def is_focused(self):
        return is_item_focused(self.name)

    @property
    def is_visible(self):
        return is_item_visible(self.name)

    @property
    def is_toggled_open(self):
        return is_item_toggled_open(self.name)

    @property
    def is_activated(self):
        return is_item_activated(self.name)

    @property
    def is_deactivated(self):
        return is_item_deactivated(self.name)

    @property
    def is_edited(self):
        return is_item_edited(self.name)

    @property
    def is_clicked(self):
        return is_item_clicked(self.name)

    @property
    def is_container(self):
        return is_item_container(self.name)

    @property
    def is_deactivated_after_edit(self):
        return is_item_deactivated_after_edit(self.name)