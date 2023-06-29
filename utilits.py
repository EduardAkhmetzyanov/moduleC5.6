import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CryproConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(
            f'https://api.currencyapi.com/v3/latest?apikey=Ah87ZzQ98DdyYkjK4shwGX9tDsbYBZosvlm4NBRq&currencies={base_ticker}&base_currency={quote_ticker}')
        total_base = json.loads(r.content)['data'][keys[base]]['value'] * float(amount)

        return total_base