# import libraries from django
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # create a simple html page as a string
    template = '<html>' \
    'this is your first view' \
    '</html>'

    return HttpResponse(content = template)