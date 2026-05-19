from django.db import models

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    UserID = models.IntegerField()
    OrderDate = models.DateField()
    ItemName = models.CharField(max_length=255)
    OrderQty = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    DeliveryAddress = models.TextField()

    def __str__(self):
        return f"Order {self.OrderID} - {self.ItemName}"