from django.db import models
from django.contrib.auth.models import User
from settings.models import GenderChoice

# Create your models here.
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='teacher_profile_pics', blank=True)
    date_of_birth = models.DateField()
    gender = models.ForeignKey(GenderChoice, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"