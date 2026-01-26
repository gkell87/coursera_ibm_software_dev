# import libraries from django
from django.shortcuts import render
from dhango.http import HttpResponse


def index(request):
    # create a simple html page as a string
    template = '<html>' \
    'this is your first view' \
    '</html>'

    returnHttpResponse(content = template)