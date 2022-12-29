from typing import Any


class BaseField:
    _name = None
    default = None

    def __init__(self, name=None,
                 default=None):
        self.name = name
        self.name = default

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def fetch(self, obj, data) -> Any:
        return self.default
