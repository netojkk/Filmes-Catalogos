from django.db import models

class Filme(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(default='https://via.placeholder.com/150')
    year = models.IntegerField()

    def __str__(self):
        return self.title
