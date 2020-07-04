from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def movie_list(request):
    movies = Movie.objects.all()
    count = len(movies)
    context = {
        'movie_list': movies,
        'movie_count': count
    }
    return render(request, 'ticketing/movie_list.html', context)


def cinema_list(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinemas':cinemas
    }
    return render(request, 'ticketing/cinema_list.html', context)