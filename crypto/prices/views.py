from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from cryptocompare.main import get_prices


def index(request):
    return HttpResponse('Hello, world. You are at the prices app index.')


class CryptoView(APIView):
    def post(self, request):
        base = request.data.get('base', '')
        quote = request.data.get('quote', '')

        content = get_prices(base, quote)
        return Response(content)
