from django.db import models
# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=20, default=None)
    description = models.TextField(default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    class Meta:
        db_table = 'Services'
    def __str__(self):
        return f"{self.name}"

class Reservation(models.Model):
    name = models.CharField(max_length=20, default=None)
    time = models.TimeField(default=None)
    date = models.DateField(default=None)
    class Meta:
        db_table = 'Reservation'
    
    def __str__(self):
        return f"{self.name} - {self.date} - {self.time}"
    