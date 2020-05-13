from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    "This will contain the inforamtion of the student"
    reg_no = models.BigIntegerField(
        verbose_name = "Registration Number", 
        help_text = "It is the registration number allocated by BPUT", 
        primary_key = True, 
        unique = True, 
        editable = True,
    )
    authAccount = models.ForeignKey(
        User, 
        verbose_name="Authenticate Account", 
        on_delete=models.CASCADE,
        related_name="studAcc"
        )
    firstName = models.CharField(
        verbose_name="First Name", 
        max_length=60,
    )
    lastName = models.CharField(
        verbose_name="Last Name", 
        max_length=60,
    )
    
    college_id = models.CharField(
        verbose_name = "College Roll No",
        help_text = "It is the college assigned Roll No.",
        unique = True,
        max_length = 8
    )
    email = models.EmailField(
        verbose_name = 'E-Mail',
        help_text = "Enter Your E-Mail",
        max_length = 254
    )
    mobile = models.BigIntegerField(
        verbose_name='Personal Contact',
        help_text="Enter your Personal Contact",
        unique=True
    )
    yoj = models.DateField(
        verbose_name = "YOJ",
        help_text = "Select your year of join the college",
    )


    @property
    def yearTravel(self):
        "this will return the Year Traveling in"
        data = str(self.yoj.year - timezone.now().year + 1)
        dic  = {
            "1":"First Year",
            "2":"Second Year",
            "3":"Third Year",
            "4":"Fourth Year",
        }
        return dic.get(data, "Not Studying")

    @property
    def fullName(self):
        "this wil return the fullName"
        return f"{self.firstName} {self.lastName}"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
