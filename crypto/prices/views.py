import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from cryptocompare.main import get_prices


def index(request):
	return HttpResponse('Hello, world. You are at the prices app index.')


@method_decorator(csrf_exempt, name='dispatch')
class CryptoView(View):

	def post(self, request):
		content = get_prices('ETH', 'BTC')
		return HttpResponse(json.dumps(content), content_type='application/json')
