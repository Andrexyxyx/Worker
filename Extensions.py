import json
import requests

from Config import keys


class APIException(Exception):
    pass

class MoneyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: float):
        if quote == base:
            raise APIException(f'''Невозможно конвертировать одинаковые валюты:
"{base}" - "{quote}"''')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'''Не удалось обработать валюту "{quote}"''')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'''Не удалось обработать валюту "{base}"''')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base