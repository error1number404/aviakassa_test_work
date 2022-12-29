from fields.MethodField import MethodField
from models import Flight, FlightBaggage, TransportBaggage
from serializers.ProviderLegSerializer import ProviderLegSerializer
from serializers.base import BaseSerializer
from utils.utils import get_min_size


class FlightSerializer(BaseSerializer):
    _model = Flight
    id = MethodField()
    price = MethodField()
    is_refundable = MethodField()
    is_changeable = MethodField()
    is_travel_policy_compliant = MethodField()
    legs = ProviderLegSerializer(many=True)
    fare_family = MethodField()
    baggage_summary = MethodField()

    def _get_context(self, data):
        return data['product']

    def get_id(self, data):
        return data['flight']['id']

    def get_price(self, data):
        return data['flight']['price']['RUB']['amount']

    def get_is_refundable(self, data):
        return data['tickets'][0]['can_be_refunded']

    def get_is_changeable(self, data):
        return True

    def get_is_travel_policy_compliant(self, data):
        return data['is_travel_policy_compliant']

    def get_fare_family(self, data):
        return data['flight']['fare_family_flag']

    def get_baggage_summary(self, data):
        return FlightBaggage(
            baggage=self.get_baggage(data['flight']['segments']),
            hand_baggage=self.get_cbaggage(data['flight']['segments'])
        )

    def get_baggage(self, data: list[dict]) -> TransportBaggage:
        min_piece = data[0]['baggage']['piece']
        min_weight = data[0]['baggage']['weight']
        for item in data:
            if item['baggage']['piece'] is None:
                min_piece = None
            else:
                min_piece = item['baggage']['piece']

            if item['baggage']['weight'] is None:
                min_weight = None
            else:
                min_weight = item['baggage']['weight']
        return TransportBaggage(quantity=min_piece,
                                weight=min_weight)

    def get_cbaggage(self, data: list[dict]) -> TransportBaggage:
        min_piece = data[0]['cbaggage']['piece']
        min_weight = data[0]['cbaggage']['piece']
        min_dimensions = data[0]['cbaggage']['dimensions']
        for item in data:
            if item['baggage']['piece'] is None:
                min_piece = None
            else:
                min_piece = item['baggage']['piece']

            if item['baggage']['weight'] is None:
                min_weight = None
            else:
                min_weight = item['baggage']['weight']
            min_dimensions = get_min_size(min_dimensions,
                                          item['cbaggage']['dimensions'])
        return TransportBaggage(quantity=min_piece,
                                weight=min_weight,
                                dimensions=min_dimensions)
