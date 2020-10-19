from typing import Callable, Any, Optional, Tuple, Union, List

from dearpygui.core import add_input_float, add_same_line, add_input_float2, add_input_float3, add_input_float4
from ..element import Element

__all__ = [
    'FloatInput'
]

_FloatDefault = Union[
    float,
    Tuple[float],
    Tuple[float, float],
    Tuple[float, float, float],
    Tuple[float, float, float, float],
    List[float],
]


class FloatInput(Element):
    _VALUE_COUNTS = {1, 2, 3, 4}

    def __init__(self, name: str, default_value: _FloatDefault = None,
                 readonly: bool = False,
                 callback_on_enter: bool = True,
                 callback: Callable[[str, Any], None] = lambda _, __: None,
                 callback_data: Optional[Any] = None,
                 count: int = 1,
                 **config):

        self.count = count
        self._validate_count()

        if default_value is None:
            self.default_value = 0 if count == 1 else ([0] * self.count)
        else:
            self.default_value = default_value

        self._validate_default()

        super().__init__(name,
                         default_value=self.default_value,
                         callback=self.on_number_changed,
                         on_enter=callback_on_enter,
                         callback_data=callback_data,
                         readonly=readonly,
                         **config)
        self.callback = callback
        self.callback_data = callback_data

    def on_number_changed(self, sender, data):
        if self.callback is not None:
            self.callback(sender, data)

    def place(self, same_line=False):
        if same_line:
            add_same_line()
        if self.count == 1:
            add_func = add_input_float
        elif self.count == 2:
            add_func = add_input_float2
        elif self.count == 3:
            add_func = add_input_float3
        elif self.count == 4:
            add_func = add_input_float4
        else:
            raise ValueError(f'unable to add/create intinput, bad count: {self.count}')

        add_func(self.name, **self.default_config)
        return self

    def _validate_count(self):
        if self.count not in self._VALUE_COUNTS:
            raise ValueError(f'count for IntInput must be in {self._VALUE_COUNTS}, actual value: {self.count}')

    def _validate_default(self):
        length = 1 if isinstance(self.default_value, int) else len(self.default_value)
        if length != self.count:
            raise ValueError(f'invalid default_value count, length must match count')
