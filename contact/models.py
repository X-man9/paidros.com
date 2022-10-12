from django.db import models

# Create your models here.

class ContactDetails(models.Model):
    # location = 
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=50, null=True)


    def __str__(self):
        return str(self.id)