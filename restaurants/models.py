from django.db import models
import uuid
from users.models import Profile

# Create your models here.
class Restaurant(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    max_num_purchases = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name
    
class Ticket(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    