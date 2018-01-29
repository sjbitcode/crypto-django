import csv
import datetime
import requests


CRYPTOCOMPARE_API_URL = 'https://www.cryptocompare.com/api/data/coinsnapshot/'


def endpoint(base, quote):
    '''
    Return dictionary with api data.
    '''
    try:
        data = requests.get(
            CRYPTOCOMPARE_API_URL,
            params={'fsym': base, 'tsym': quote}
        )
        return data.json()
    except:
        return {}


def extract_exchanges_data(data):
    '''
    Return list of dictionaries.
    Each dictionary has info about an exchange.
    '''

    return data.get('Data', {}).get('Exchanges', [])


def clean_data(exchanges_data):
    '''
    Remove unwanted info from exchanges data.
    Rename dict keys.
    '''

    if len(exchanges_data) == 0:
        print('No exchanges data')
        return

    filename = '{}.csv'.format(
        datetime.datetime.now().strftime("%Y-%m-%d--%H:%M:%S")
    )

    cleaned_data = []
    for exchange in exchanges_data:
        cleaned_data.append({
            'Exchange': exchange.get('MARKET'),
            'Base': exchange.get('FROMSYMBOL'),
            'Quote': exchange.get('TOSYMBOL'),
            'Price': exchange.get('PRICE'),
            'High': exchange.get('HIGH24HOUR'),
            'Low': exchange.get('LOW24HOUR'),
            'Volume': exchange.get('VOLUME24HOUR')
        })
    return cleaned_data


def get_prices(base, quote):

    data = endpoint(
        base=base,
        quote=quote
    )
    exchanges = extract_exchanges_data(data)
    return clean_data(exchanges)

