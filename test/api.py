from data import TEST_AVIA_SERVICE_DETAILS_RESPONSE


class AviaApi:
    def get_flights(self):
        """
        Тут условно делаем запрос в апи и получаем результат
        :return:
        """
        return TEST_AVIA_SERVICE_DETAILS_RESPONSE


avia_api = AviaApi()
