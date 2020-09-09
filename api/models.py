from django.db import models

# Create your models here.

class Taks(models.Model):
    title = models.CharField(max_length=150)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title