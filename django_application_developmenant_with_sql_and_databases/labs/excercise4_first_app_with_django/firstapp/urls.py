from django.contrib import admin
from django.urls import include, path

urlpatterns = [# create path object defining the URL patters
                path(route = '', veiw = veiws.index, name = 'index')]