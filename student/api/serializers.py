from rest_framework import serializers 
from ..models import Student
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    "This the serializer for the model : User"
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
        ]
        extra_kwargs = {
            "password" :{
                "write_only":True
            },
            "id" :{
                "read_only":True
            }
        }

class StudentSerializer(serializers.ModelSerializer):
    "This the serializer for the model : Student"
    authAccount = UserSerializer()
    class Meta:
        model = Student
        fields = [
            "authAccount",
            "firstName",
            "lastName",
            "reg_no",
            "college_id",
            "email",
            "mobile",
            "yoj",
            "yearTravel",
            "fullName"
        ]
        extra_kwargs = {
            "firstName" :{
                "write_only":True
            },
            "lastName" :{
                "write_only":True
            },
            "yoj" : {
                "write_only":True
            }
        }
    
    def create(self, validated_data):
        "This will create the instance for many to many field " 
        acc  = validated_data.pop("authAccount", None)
        if not acc:
            msg = "PLease provide the information of the Student"
            raise ValidationError(msg)
        username= acc.pop("username", None)
        if not username:
            msg = "Please provide the username of the User"
            raise ValidationError(msg)
        password = acc.pop("password", None)
        if not password:
            msg = "Please provide the password of the User"
            raise ValidationError(msg)
        user = User.objects.create(
            username=username
        )
        user.set_password(password)
        user.save()

        student = Student.objects.create(authAccount = user, **validated_data)

        return student
    
    def upadate(self, instance, validated_data):
        "This is the update or put haeader for the file"
        instance.mobile = validated_data.get("mobile", instance.mobile)
        instance.email = validated_data.get("email", instance.email)
        return instance