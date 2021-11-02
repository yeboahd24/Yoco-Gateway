from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.FloatField(max_length=100)

    def __str__(self) -> str:
        return str(self.amount)