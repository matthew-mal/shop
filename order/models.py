from django.db import models


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=120)
    postal_code = models.PositiveIntegerField()
    city = models.CharField(max_length=150)

    def __str__(self):
        return self.first_name
