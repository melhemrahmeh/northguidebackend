from django.db import models
import uuid
    
class ContactRequest(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 100)
    phoneNumber = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    
class VolunteeringOpportunity(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position = models.CharField(max_length=100)
    description =  models.CharField(max_length = 1000)
    
class VolunteeringApplication(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    volunteeringOpportunity =  models.ForeignKey(VolunteeringOpportunity, on_delete = models.CASCADE, default="")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 100)
    phoneNumber = models.CharField(max_length=20)