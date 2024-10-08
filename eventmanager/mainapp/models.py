# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'

class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    location = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'event'

class Attendee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'attendee'
