from django.db import models
from author.models import Author

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return  f'{self.title} -> {self.author if self.author else None}'

