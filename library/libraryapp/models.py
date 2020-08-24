from django.db import models

# Create your models here.

class Library(models.Model):
    library_name = models.CharField('library name', max_length=100)
    creation_date = models.DateTimeField('date created')

class Book(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)