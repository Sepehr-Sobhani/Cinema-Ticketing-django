from django.urls.conf import path
from .views import *

app_name = 'ticketing'

urlpatterns = [
    path('movie/list', movie_list, name='movie_list'),
    path('cinema/list', cinema_list, name='cinema_list')
]