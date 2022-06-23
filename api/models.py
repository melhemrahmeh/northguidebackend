from django.db import models
import uuid

class Items(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=255)
    subcatgeory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    
class ContactRequests(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 255)
    phoneNumber = models.CharField(max_length=13)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    
class VolunteeringOpportunities(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position = models.CharField(max_length=255)
    description =  models.CharField(max_length = 200)
    
class VolunteeringApplications(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    volunteeringOpportunity =  models.ForeignKey(VolunteeringOpportunities, on_delete = models.CASCADE, default="")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 255)
    phoneNumber = models.CharField(max_length=13)
    description =  models.CharField(max_length = 200)