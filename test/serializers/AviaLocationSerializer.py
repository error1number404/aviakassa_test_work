from fields.MethodField import MethodField
from models import Loc, ObjectType, AviaLocation
from serializers.BaseLocationSerializer import BaseLocationSerializer


class AviaLocationSerializer(BaseLocationSerializer):
    _model = AviaLocation
    airport = MethodField()
    terminal = MethodField()
    context_key = ''

    def __init__(self, context_key, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context_key = context_key

    def _get_context(self, data: dict) -> dict:
        return data[self.context_key]

    def get_airport(self, data):
        return Loc(type=ObjectType.airport,
                   name=data['airport']['title'])

    def get_terminal(self, data):
        return Loc(type=ObjectType.terminal,
                   name=data['terminal'])
