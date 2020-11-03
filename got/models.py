from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=255)
    pic = models.CharField(max_length=1000, null=True)
    
    def __str__(self):
        return self.name
class Title(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Character(models.Model):
    STATUS = (
        ('Dead', 'Dead'),
        ('Alive', 'Alive'),
    )
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    house = models.ForeignKey(House, related_name="members", on_delete=models.PROTECT)
    pict = models.CharField(max_length=1000, null=True)
    appearances = models.PositiveIntegerField(null=True)
    status = models.CharField(max_length=5, choices=STATUS)
    age = models.PositiveIntegerField(null=True)
    titles = models.ManyToManyField(Title, related_name="characters", blank=True)
    weapon = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.first