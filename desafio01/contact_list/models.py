from django.db import models


# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=64)
    favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"
