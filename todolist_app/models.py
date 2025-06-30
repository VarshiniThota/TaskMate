from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasklist(models.Model) :
    manage=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    tasks=models.CharField(max_length=300)
    done=models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.tasks    
