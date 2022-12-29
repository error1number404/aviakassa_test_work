from typing import Iterable

from pydantic import BaseModel

from fields.MethodField import MethodField
from models import ProviderLeg
from serializers.ProviderSegmentSerializer import ProviderSegmentSerializer
from serializers.base import BaseSerializer


class ProviderLegSerializer(BaseSerializer):
    _model = ProviderLeg
    segments = ProviderSegmentSerializer(many=True)
    segments_count = MethodField()
    route_duration = MethodField()
    is_round = False

    def _get_context(self, data: dict) -> dict:
        context = data["flight"]["segments"]
        if context[0]['departure']['airport']['id'] == \
                context[-1]['arrival']['airport']['id']:
            self.is_round = True
        return context

    def serialize(self, data: Iterable) -> tuple[BaseModel, ...]:
        data = self._get_context(data)
        if not callable(getattr(data, "__iter__")):
            raise Exception("Is not iterable")
        if not self.is_round:
            return (self.serialize_one(data),)
        return (self.serialize_one(data[:len(data) // 2]),
                self.serialize_one(data[len(data) // 2:]))

    def get_segments_count(self, data):
        return len(data)

    def get_route_duration(self, data):
        return sum(item['route_duration'] for item in data)
