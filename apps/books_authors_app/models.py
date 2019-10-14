from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Book object: {self.title}"

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name="authors")
    last_name = models.CharField(max_length=45)
    notes = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models. DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Author object: {self.first_name} {self.last_name}"



# Create your models here.
