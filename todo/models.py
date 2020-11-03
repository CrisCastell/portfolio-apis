from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    isCompleted = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    isEdited = models.BooleanField(default=False)

    def __str__(self):
        return self.title