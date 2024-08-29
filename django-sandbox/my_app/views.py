from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):

    return HttpResponse("Hello World")


def about(request):

    return HttpResponse("Hi, my name is Sid!")


def say_hello(request, first_name):

    return HttpResponse(f"Hello {first_name}!")


def add_nums(request, number_1, number_2):

    return HttpResponse(f"SUM : {number_1 + number_2}")