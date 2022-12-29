from fields.MethodField import MethodField
from models import Loc, ObjectType, BaseLocation
from serializers.base import BaseSerializer


class BaseLocationSerializer(BaseSerializer):
    _model = BaseLocation
    country = MethodField()
    city = MethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_country(self, data):
        return Loc(type=ObjectType.country,
                   name=data['country']['title'])

    def get_city(self, data):
        return Loc(type=ObjectType.city,
                   name=data['city']['title'])
