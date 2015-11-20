"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Author(models.Model):
    AuthorID = models.CharField(max_length = 10, blank = False, primary_key = True)
    Name = models.CharField(max_length = 20, blank = False)
    Age = models.CharField(max_length = 3, blank = True)
    Country = models.CharField(max_length = 10, blank = True)
    ST = models.IntegerField(default = 0)


class Book(models.Model):
    ISBN = models.CharField(max_length = 13, blank = False, primary_key = True)
    Title = models.CharField(max_length = 50,blank = True)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 20, blank = True)
    PublishDate = models.DateField()
    Price = models.CharField(max_length = 8, blank = True)
    ST = models.IntegerField(default = 0);

    