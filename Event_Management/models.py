from django.db import models

# Create your models here.
class Booking(models.Model):
    event_name = models.CharField(max_length=40)
    name = models.CharField(max_length=30)
    email = models.EmailField(default=False)
    phone = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

