from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):

    context = {

                'movies' : ["The Usual Suspects", "Casino Royale", "Ghost Protocol"]

              }

    return render(request, "movie_app/index.html", context)