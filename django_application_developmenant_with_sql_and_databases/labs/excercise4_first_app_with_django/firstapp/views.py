# import libraries from django
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse


def get_daate(request):
    # create a simple html page as a string
    template = '<html>' \
    'this is your first view' \
    '</html>'

    return HttpResponse(content = template)

def get_date(request):
    today = date.today()
    template = "<html>" \
    "today's data {} " \
    "</html>".format(today)

    return HttpResponse(content = template)