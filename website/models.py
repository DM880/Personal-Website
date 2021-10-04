from django.db import models

# Create your models here.

class ContactDetail(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.name.title()