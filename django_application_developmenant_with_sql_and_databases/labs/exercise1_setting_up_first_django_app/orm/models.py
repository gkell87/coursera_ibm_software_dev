from django.db import models

# Define your first model from here:
class User(models.Model):
    # Charfield for users first name
    first_name = models.Charfield(null = False, max_lengh = 30, default = 'John')
    
    # Charfield for last name
    last_name models.Charfield(null = False, max_length = 30, defualt = 'Doe')

    # Charfield for DOB
    dob = models.DataField(null = True)