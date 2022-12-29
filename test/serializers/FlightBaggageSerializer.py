from fields.MethodField import MethodField
from models import FlightBaggage, TransportBaggage
from serializers.base import BaseSerializer


class FlightBaggageSerializer(BaseSerializer):
    _model = FlightBaggage
    baggage = MethodField()
    hand_baggage = MethodField()

    def get_baggage(self, data):
        data = data['baggage']
        return TransportBaggage(quantity=data['piece'],
                                weight=data['weight'])

    def get_hand_baggage(self, data):
        data = data['cbaggage']
        return TransportBaggage(quantity=data['piece'],
                                weight=data['weight'],
                                dimensions=data['dimensions']
                                )
