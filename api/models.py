from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid

class Item(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=255)
    subcatgeory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
  
    def __str__(self) -> str:
        return self.name
    
    
    
class ContactRequest(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 255)
    phoneNumber = PhoneNumberField(unique = True, null = True, blank = False) # Here
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    
    
class VolunteeringForm(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 255)
    phoneNumber = PhoneNumberField(unique = True, null = True, blank = False) # Here
    position = models.CharField(max_length=255)