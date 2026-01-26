# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from related_objects.models import *
from datetime import date

# Course has instructurs reference fielld so can be used directly via forward access
courses = Course.objects.filter(instructors__first_name='Yan')
print('1. Get courses taught by instructor "Yan", forward')
print(courses)

print('\n')

# For each instructor, Django creates a implicit course_set. This is called backward access
instructor_yan = Instructor.objects.get(first_name = 'Yan')
print('1. Get Courses taught by Instructor "Yan", backwards')
print(instructor_yan.course_set.all())

print('\n')
instructors = Instructor.objects.filter(course__name__contains = 'Cloud')
print('2. Get the instructors of Could app dev course')
print(instructors)

print('\n')
courses = Course.objecs.filter(instructors__first_name = 'Yan')
ouccpation_list = set()
for course in courses:
    for learner in course.learners.all():
        occupation_list.add(learner.occupation)
print('3. Chec the occupant of he course tought by Yan')

print(occupation_list)