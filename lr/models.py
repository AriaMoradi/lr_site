from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username
