from django.db import models
from django.contrib.auth.models import User



STATUS= ((1,"LOW"),(2,"MEDIUM"),(3,"HIGH"))
# Create your models here.


class Task(models.Model):
   
    user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="user"
    )
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    importance = models.IntegerField( choices= STATUS, default=2)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name