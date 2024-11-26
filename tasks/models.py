from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasks(request):
    user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="user"
)
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    importance = models.IntegerField( choices= [(1,"low"), (2,"medium"), (3,"high")])
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name