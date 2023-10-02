from django.db import models

# Create your models here.
class GenderChoice(models.Model):
    label = models.CharField(max_length=20)
    code = models.CharField(max_length=1, unique=True)

    def __str__(self) -> str:
        return self.label