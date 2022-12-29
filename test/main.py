from serializers.FlightSerializer import FlightSerializer
from api import avia_api
from models import Flight


class AviaConverter:

    def convert(self, data: dict) -> Flight:
        serializer = FlightSerializer()
        result = serializer.serialize(data=data)
        return result


def main():
    converter = AviaConverter()
    result = avia_api.get_flights()
    return converter.convert(result)


if __name__ == '__main__':
    main()
