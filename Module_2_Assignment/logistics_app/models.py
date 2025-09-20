from django.db import models

#from .ai_engine import calculate_eta_mock
#class Order(models.Model):
#    order_id = models.CharField(max_length=20, unique=True)
#    order_date = models.DateField()
#    delivery_location = models.CharField(max_length=255)
#    client_type = models.CharField(max_length=100)

#    def __str__(self):
#        return f"{self.order_id} ({self.client_type})"

class Order(models.Model):
    order_id = models.CharField(max_length=20, unique=True)
    order_date = models.DateField()
    delivery_location = models.CharField(max_length=255)
    client_type = models.CharField(max_length=100)
    eta = models.CharField(max_length=100, blank=True, null=True)  # New field

    def __str__(self):
        return f"{self.order_id} ({self.client_type})"
