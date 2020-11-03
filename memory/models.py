from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=255)
    fact = models.TextField(null=True)
    pic = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def serialize(self):
        return {
            "name": self.name,
            "value":self.id,
            "fact": self.fact,
            "pic":self.pic
        }