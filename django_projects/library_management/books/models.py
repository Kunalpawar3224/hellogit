from django.db import models

# Create your models here.

class Books(models.Model):
    book_name = models.CharField(max_length=100)
    book_unique_id = models.PositiveSmallIntegerField()
    author_name = models.CharField(max_length=100)  # sometimes single book have mutiple authors
    publication_information = models.TextField()
    book_version = models.FloatField()

