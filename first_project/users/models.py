from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    avartar = models.CharField(max_length=50)
    
    def _str_(self):
        return self.name

