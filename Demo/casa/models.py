from django.db import models

# Create your models here.


class Casa(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return self.name
