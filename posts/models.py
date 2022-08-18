from pyexpat import model
from django.db import models


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:12] + "..."
