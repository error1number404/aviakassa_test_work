from typing import Callable

from fields.base import BaseField


class MethodField(BaseField):
    func: Callable = None

    def __init__(self, func: Callable = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.func = func

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self._name is None:
            self._name = f"get_{value}"
            return
        self._name = value

    def fetch(self, obj, data):
        if self.func is not None:
            return self.func(data)

        func = getattr(obj, self._name)

        if not callable(func):
            raise Exception(f'{self._name} is not callable')
        return func(data)
