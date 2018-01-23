import json

from django.shortcuts import render
from django.http import HttpResponse

from cryptocompare.main import get_prices


def index(request):
	return HttpResponse('Hello, world. You are at the prices app index.')


def get_cryptos(request):
	content = get_prices('ETH', 'BTC')

	response = HttpResponse(json.dumps(content), content_type='application/json')
	return response