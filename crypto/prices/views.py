from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cryptocompare import get_prices
from .serializers import CryptoPairSerializer


def index(request):
    return HttpResponse('Hello, world. You are at the prices app index.')


class CryptoView(APIView):
    def post(self, request):
        serializer = CryptoPairSerializer(data=request.data)

        if serializer.is_valid():
            base = serializer.validated_data.get('base', '')
            quote = serializer.validated_data.get('quote', '')

            content = get_prices(base, quote)
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
