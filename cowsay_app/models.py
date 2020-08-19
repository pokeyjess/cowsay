from django.db import models

class Input(models.Model):
    input = models.TextField()

    def __str__(self):
        return self.input
