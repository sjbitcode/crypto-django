from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('get-cryptos', views.CryptoView.as_view(), name='get-cryptos')
]
