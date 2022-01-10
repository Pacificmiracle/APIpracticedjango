from django.db import models

# Create your models here.
class Entry(models.Model):
    ID = models.CharField(max_length=10,primary_key=True)
    Name = models.CharField(max_length=50)
    Number = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.Name
    
    
    