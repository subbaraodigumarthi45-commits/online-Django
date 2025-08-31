from django.db import models

class Exam(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    # Add other fields as needed