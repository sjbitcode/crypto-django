from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('get-cryptos', views.get_cryptos, name='get-cryptos')
]