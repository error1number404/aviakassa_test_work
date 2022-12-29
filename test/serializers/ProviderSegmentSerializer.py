from datetime import datetime

from fields.MethodField import MethodField
from models import ProviderSegment, ClassAvia, ObjectType, BaseInfo
from serializers.AviaLocationSerializer import AviaLocationSerializer
from serializers.FlightBaggageSerializer import FlightBaggageSerializer
from serializers.base import BaseSerializer

class_name_to_enum = {
    'E': 'economy',
    'B': 'business',
    'F': 'first',
    'C': 'comfort',
}


class ProviderSegmentSerializer(BaseSerializer):
    _model = ProviderSegment
    arrival = AviaLocationSerializer(context_key='arrival')
    arrival_at = MethodField()
    arrival_at_utc = MethodField()
    arrival_at_timezone_offset = MethodField()
    departure = AviaLocationSerializer(context_key='departure')
    departure_at = MethodField()
    departure_at_utc = MethodField()
    departure_at_timezone_offset = MethodField()
    seats = MethodField()
    flight_number = MethodField()
    flight_duration = MethodField()
    transfer_duration = MethodField()
    comment = MethodField()
    baggage = FlightBaggageSerializer()
    flight_class = MethodField()
    carrier = MethodField()
    fare_code = MethodField()
    aircraft = MethodField()

    def get_arrival_at(self, data):
        return datetime.strptime(
            data['arrival']['datetime'],
            '%d.%m.%Y %H:%M:%S')

    def get_arrival_at_utc(self, data):
        return data['arrival']['timestamp']

    def get_arrival_at_timezone_offset(self, data):
        return data['arrival']['timezone_offset']

    def get_departure_at(self, data):
        return datetime.strptime(
            data['departure']['datetime'],
            '%d.%m.%Y %H:%M:%S')

    def get_departure_at_utc(self, data):
        return data['departure']['timestamp']

    def get_departure_at_timezone_offset(self, data):
        return data['departure']['timezone_offset']

    def get_seats(self, data):
        return data['seats']

    def get_flight_number(self, data):
        return data['flight_number']

    def get_flight_duration(self, data):
        return data['route_duration']

    def get_transfer_duration(self, data):
        return 0

    def get_comment(self, data):
        return data['comment']

    def get_fare_code(self, data):
        return data['fare_code']

    def get_flight_class(self, data):
        return getattr(ClassAvia,
                       class_name_to_enum[data['class']['name']])

    def get_aircraft(self, data):
        return BaseInfo(type=ObjectType.aircraft,
                        id=data['aircraft']['code'],
                        name=data['aircraft']['title'])

    def get_carrier(self, data):
        return BaseInfo(type=ObjectType.carrier,
                        id=data['carrier']['id'],
                        name=data['carrier']['title'])
