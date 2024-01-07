from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task_model(models.Model):
    name=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    complete=models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name