from django.db import models
import uuid


class Tourist(models.Model):
    _id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Location(models.Model):
    _id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Place(models.Model):
    _id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    rating = models.IntegerField()

    def __str__(self):
        return self.name
