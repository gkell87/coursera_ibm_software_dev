# import libraries from django
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # create a simple html page as a string
    template = '<html>' \
    'this is your first view' \
    '</html>'

    return HttpResponse(content = template)

def get_date(request):
    today = date.today()
    template = "<html>" \
                "Today's date is {}" \
               "</html>".format(today)
    return HttpResponse(content = template)  