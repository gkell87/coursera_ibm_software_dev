# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date


# Your code starts from here:
def write_instructors():
    user_john = User(first_name = 'John', last_name = 'Doe', dob = date(1962, 7, 16))
    user_john.save()
    instructor_john = Instructor(full_time = True, total_learners = 30050)
    # Update user reference of instructor john
    instructor_john.user = user_john
    instructor_john.save()

    instructor_yan = Instructor(first_name = 'Yan', last_name = 'Lou', dob = date(1962, 7, 16), full_time = True, total_learners = 30050)
    instructor_yan.save()
    instructor_joy = Instructor(first_name='Joy', last_name='Li', dob=date(1992, 1, 2), full_time=False, total_learners=10040)
    instructor_joy.save()
    instructor_peter = Instructor(first_name='Peter', last_name='Chen', dob=date(1982, 5, 2), full_time=True, total_learners=2002)
    instructor_peter.save()
    print("Instructor objects all saved... ")