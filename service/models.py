from django.db import models
from datetime import timedelta
from django.core.exceptions import ValidationError
# Create your models here.
class Service(models.Model):
    "This will hold the information of the service"
    bus_no = models.IntegerField(
        verbose_name = "Bus Number",  
        primary_key = True, 
        unique = True, 
        editable = True,
    )    
    startTime = models.DateTimeField(
        verbose_name="Start Time"
    )
    places = models.TextField(
        verbose_name="Places",
        help_text="Comman Separated Value",
    )
    time = models.TextField(
        verbose_name="Time",
        help_text="Comman Separated Value",
    )
    CurrentLocation = models.CharField(
        verbose_name="Current Location", 
        max_length=100,
        default="",
        blank=True
    )

    def option(self):
        places = self.places.split(",")
        times = [self.startTime + timedelta(minutes=int(i)) for i in self.time.split(",")]
        times = [i.strftime("%I:%M, %p") for i in times]
        return dict(zip(places, times))

    def clean(self):
        l = self.places.split(",")
        k = self.time.split(",")

        if len(l) != len(k):
            raise ValidationError("Enter Correct Places and Time Buffer")

    

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"

