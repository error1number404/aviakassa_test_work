from typing import Type, Iterable

from pydantic import BaseModel

from fields.base import BaseField


class BaseSerializer:
    _model: Type[BaseModel]
    many = False

    def __init__(self, many=False):
        self.many = many
        for item in dir(self):
            value = getattr(self, item)
            if issubclass(type(value), BaseField):
                if value.name is None:
                    value.name = item

    def _get_context(self, data: dict) -> dict:
        return data

    def serialize(self, data: dict | Iterable) -> \
            tuple[BaseModel, ...] | BaseModel:
        data = self._get_context(data)
        if self.many:
            if not callable(getattr(data, "__iter__")):
                raise Exception("Is not iterable")
            return tuple(self.serialize_one(item) for item in data)
        return self.serialize_one(data=data)

    def serialize_one(self, data) -> BaseModel:
        fetched_data = {}
        for field in self._model.__fields__:
            _field = getattr(self, field)
            if _field is None:
                continue
            if issubclass(type(_field), BaseSerializer):
                fetched_data[field] = _field.serialize(data=data)
                continue
            fetched_data[field] = _field.fetch(self, data=data)
        return self._model(**fetched_data)
